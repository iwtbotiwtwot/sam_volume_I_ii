"""Verify the delivered reader and reproduce it in a fresh relocated tree."""
from pathlib import Path
import hashlib,importlib.metadata,json,re,shutil,subprocess,sys,tempfile
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent
PKG=BASE.parent
sys.path.insert(0,str(BASE))
from content import PAGES,CLOSURE_TEXT
from continuation_content import PAGES as PREVIOUS
PDF=PKG/'output/pdf/SAM_Volume_I_Chapter_II_Physical_Development_Draft_20261015.pdf'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
checks=[]
def ok(name,test):
    assert test,name
    checks.append(name)
reader=PdfReader(PDF)
ok('twenty rendered pages',len(reader.pages)==len(PAGES)==20)
ok('first14 sections preserved verbatim',PAGES[:7]==PREVIOUS[:7])
text='\n'.join(page.extract_text() for page in reader.pages)
for n in range(1,41):ok('section '+str(n),bool(re.search(r'\b'+str(n)+r'\.\s',text)))
for target in ['23,482,368','6,558,008','1085537','rank 14','rank two','atan2','V13']:
    ok('current result '+target,target in text)
metrics=json.loads((BASE/'LAYOUT.json').read_text())
ok('forty frames',len(metrics)==40)
ok('all frames fit',all(m['unused_height']>=-0.1 for m in metrics))
fonts={}
for page in reader.pages:
    for k,v in page['/Resources']['/Font'].get_object().items():
        font=v.get_object();fd=font.get('/FontDescriptor')
        if fd:
            descriptor=fd.get_object()
            ok('font embedded '+str(font.get('/BaseFont')),any(z in descriptor for z in ['/FontFile','/FontFile2','/FontFile3']))
            fonts[str(font.get('/BaseFont'))]=str(font.get('/Subtype'))
with tempfile.TemporaryDirectory(prefix='sam-ch2-pdf-rebuild-') as d:
    target=Path(d)/'physical3';chapter=target/'chapter'
    shutil.copytree(BASE,chapter,ignore=shutil.ignore_patterns('__pycache__','PDF_VERIFICATION.json'))
    (target/'closure').mkdir()
    shutil.copy2(PKG/'closure/FINAL_CLOSURE.json',target/'closure/FINAL_CLOSURE.json')
    done=subprocess.run([sys.executable,str(chapter/'build_pdf.py')],capture_output=True,text=True)
    ok('relocated fresh-cache build exits0',done.returncode==0)
    replay=target/'output/pdf'/PDF.name
    ok('fresh-cache byte-identical rebuild',PDF.read_bytes()==replay.read_bytes())
    rebuild_sha=sha(replay)
sources=[p for p in BASE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ['PDF_VERIFICATION.json']]
ver={'schema':'SAM_CH2_PHYSICAL_READER_PDF_VERIFICATION_V1','status':'PASS',
 'pdf':{'path':str(PDF.relative_to(PKG)),'sha256':sha(PDF),'bytes':PDF.stat().st_size,'pages':len(reader.pages)},
 'sections':40,'checks_passed':len(checks),'checks':checks,'layout':metrics,
 'embedded_fonts':fonts,'relocated_fresh_cache_rebuild_sha256':rebuild_sha,
 'source_files':[{'path':str(p.relative_to(PKG)),'sha256':sha(p)} for p in sorted(sources)],
 'closure_summary':CLOSURE_TEXT,'closure_summary_sha256':hashlib.sha256(CLOSURE_TEXT.encode()).hexdigest(),
 'rendering_packages':{n:importlib.metadata.version(n) for n in ['reportlab','matplotlib','svglib','pypdf','fonttools','pillow']},
 'visual_review':{'status':'COMPLETE','tool':'Poppler100dpi and native image inspection',
  'current_pages_reviewed':[1]+list(range(8,21)),'unchanged_body_pages_2_to_7':'Retained prior visual QA; first14 sections unchanged',
  'findings':'No overflow, clipping, missing equation glyphs or table collisions. Final spin page and all new instrument/proof/endpoint pages inspected.'},
 'native_executions':0}
(BASE/'PDF_VERIFICATION.json').write_text(json.dumps(ver,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'pages':len(reader.pages),'sha256':sha(PDF),'fresh_cache_rebuild':'BYTE_IDENTICAL'}))
