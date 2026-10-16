"""Verify the source-to-field reader and byte-identical relocated rebuild."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys,tempfile,importlib.metadata
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
sys.path.insert(0,str(HERE));from content import PAGES
PDF=BASE/'output/pdf/SAM_Volume_I_Chapter_III_Source_to_Field_Development_20261015.pdf'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def ok(n,b):assert b,n;checks.append(n)
r=PdfReader(PDF);ok('fourteen pages',len(r.pages)==len(PAGES)==14)
text='\n'.join(p.extract_text() for p in r.pages)
for n in range(1,29):ok('section '+str(n),bool(re.search(r'\b'+str(n)+r'\.\s',text)))
for n,p in enumerate(r.pages,1):
 t=p.extract_text();ok('page header '+str(n),'SAM / VOLUME I / CHAPTER III' in t);ok('author footer '+str(n),'Brady / ChatGPT / Codex' in t)
source='\n'.join(left+'\n'+right for left,right in PAGES)
for a,b in [('9427','252000'),('2603','28000')]:ok('vector equation source '+a,a in source and b in source)
for t in ['2,040','822','52 assertions','45','36-coordinate','counterterm','matched internal','G224']:
 ok('current content '+t,t in text)
for t in ['correlated-phase supplement 47','independent enclosures','not a minimum lift']:
 ok('correlated comparison content '+t,t in text)
ok('shared-history phase integral retained',r'\delta\theta(T)=-\int_{nT}^{T}\nu_0(s)\,ds' in source)
ok('rational correlated bounds retained',r'-\frac{uaT}{2-a}' in source and r'-\frac{\ell aT}{2}' in source)
ok('old807 count removed','checker 807' not in text)
metrics=json.loads((HERE/'LAYOUT.json').read_text());ok('twentyeight frames',len(metrics)==28);ok('no overflow',all(m['unused_height']>=-.1 for m in metrics))
fonts=set()
for p in r.pages:
 for v in p['/Resources']['/Font'].get_object().values():
  f=v.get_object();d=f.get('/FontDescriptor')
  if d:
   ok('font embedded '+str(f.get('/BaseFont')),any(k in d.get_object() for k in ['/FontFile','/FontFile2','/FontFile3']));fonts.add(str(f.get('/BaseFont')))
with tempfile.TemporaryDirectory(prefix='sam-ch3-rebuild-') as tmp:
 dest=Path(tmp)/'campaign/chapter3';shutil.copytree(HERE,dest,ignore=shutil.ignore_patterns('__pycache__','PDF_VERIFICATION.json'))
 p=subprocess.run([sys.executable,str(dest/'build_pdf.py')],capture_output=True,text=True);ok('relocated fresh-cache build',p.returncode==0)
 replay=dest.parent/'output/pdf'/PDF.name;ok('byte-identical relocated rebuild',replay.read_bytes()==PDF.read_bytes())
result=dict(schema='SAM_CH3_READER_VERIFICATION_V1',status='PASS',checks_passed=len(checks),checks=checks,pages=len(r.pages),sections=28,pdf=dict(path=str(PDF.relative_to(BASE)),sha256=sha(PDF),bytes=PDF.stat().st_size),layout=metrics,embedded_fonts=sorted(fonts),relocated_rebuild='BYTE_IDENTICAL',rendering_packages={n:importlib.metadata.version(n) for n in ['reportlab','matplotlib','svglib','pypdf','fonttools','pillow']},visual_review='See separate VISUAL_QA.json; this script reports structural/artifact checks only')
(HERE/'PDF_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(status='PASS',checks=len(checks),pages=len(r.pages),sha256=sha(PDF))))
