#!/usr/bin/env python3
"""Verify companion contents, retained predecessor, and portable PDF rebuild."""
from pathlib import Path
import hashlib, importlib.metadata, json, re, shutil, subprocess, sys, tempfile
from pypdf import PdfReader
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
sys.path.insert(0,str(HERE))
from content import PAGES
from physical_content import PAGES as OLD
PDF=BASE/'output/pdf/SAM_Volume_I_Chapter_II_Source_to_Field_Update_20261015.pdf'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def ok(name,test):
    if not test:raise AssertionError(name)
    checks.append(name)
reader=PdfReader(PDF)
ok('24 pages',len(reader.pages)==len(PAGES)==24)
ok('all old40 sections retained verbatim',PAGES[:20]==OLD)
for row in json.loads((HERE/'INHERITED_SOURCES.json').read_text())['files']:
    frozen=HERE/row['path']
    ok('preserved source '+row['path'],sha(frozen)==row['local_sha256'])
    if row['path']=='physical_content.py':
        restored=frozen.read_text().replace("Path(__file__).resolve().parent/'FINAL_CLOSURE.json'","Path(__file__).resolve().parent.parent/'closure/FINAL_CLOSURE.json'")
        ok('original40 source differs only by portable closure path',hashlib.sha256(restored.encode()).hexdigest()==row['origin_sha256'])
    else:ok('original source bytes '+row['path'],row['origin_sha256']==row['local_sha256'])
text='\n'.join(p.extract_text() for p in reader.pages)
for n in range(1,49):ok('section '+str(n),bool(re.search(r'\b'+str(n)+r'\.\s',text)))
for s in ['23,482,368','6,558,008','1085537','V13','2.84e-9','1.39e-9','four','six']:
    ok('retained/new scope '+s,s in text)
normalized=re.sub(r'\s+',' ',text)
for phrase in ['sector-resolved effects','Its entire population-transfer history is unchanged','The counterterm part is invisible throughout']:
    ok('new exact receiving result '+phrase,phrase in normalized)
metrics=json.loads((HERE/'LAYOUT.json').read_text())
ok('48 frames',len(metrics)==48)
ok('all frames fit',all(m['unused_height']>=-.1 for m in metrics))
fonts={}
for page in reader.pages:
    for v in page['/Resources']['/Font'].get_object().values():
        f=v.get_object();fd=f.get('/FontDescriptor')
        if fd:
            d=fd.get_object();ok('embedded font '+str(f.get('/BaseFont')),any(k in d for k in ['/FontFile','/FontFile2','/FontFile3']))
            fonts[str(f.get('/BaseFont'))]=str(f.get('/Subtype'))
with tempfile.TemporaryDirectory(prefix='sam-ch2-source-field-rebuild-') as d:
    target=Path(d)/'portable';dest=target/'chapter2'
    shutil.copytree(HERE,dest,ignore=shutil.ignore_patterns('__pycache__','PDF_VERIFICATION.json'))
    done=subprocess.run([sys.executable,str(dest/'build_pdf.py')],capture_output=True,text=True)
    ok('relocated build',done.returncode==0)
    other=target/'output/pdf'/PDF.name
    ok('fresh-cache byte identical',other.read_bytes()==PDF.read_bytes())
sources=[p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PDF_VERIFICATION.json']
qa=HERE/'VISUAL_QA.json'
visual=json.loads(qa.read_text()) if qa.exists() else {'status':'PENDING','new_pages':[21,22,23,24],'changed_first_page':1}
if qa.exists():ok('visual review matches current PDF',visual['pdf_sha256']==sha(PDF))
out={'schema':'SAM_CH2_SOURCE_FIELD_PDF_VERIFICATION_V1','status':'PASS','checks_passed':len(checks),'checks':checks,'pages':24,'sections':48,'predecessor_sections_preserved':40,'pdf':{'path':str(PDF.relative_to(BASE)),'sha256':sha(PDF),'bytes':PDF.stat().st_size},'layout':metrics,'embedded_fonts':fonts,'rebuild':'RELOCATED_FRESH_CACHE_BYTE_IDENTICAL','sources':[{'path':str(p.relative_to(BASE)),'sha256':sha(p)} for p in sorted(sources)],'visual_review':visual}
(HERE/'PDF_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'pages':24,'sections':48,'sha256':sha(PDF)}))
