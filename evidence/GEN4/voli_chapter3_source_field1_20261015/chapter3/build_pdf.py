"""Deterministic Chapter III two-column reader from editable source pages."""
from pathlib import Path
import sys,json,hashlib
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
sys.path.insert(0,str(HERE))
import renderer as r
from content import TITLE,ABSTRACT,PAGES
r.OUT=BASE/'output/pdf';r.OUT.mkdir(parents=True,exist_ok=True)
r.TMP=BASE/'tmp/pdfs';r.TMP.mkdir(parents=True,exist_ok=True)
out=r.OUT/'SAM_Volume_I_Chapter_III_Source_to_Field_Development_20261015.pdf'
c=canvas.Canvas(str(out),pagesize=r.PAPER,pageCompression=1,invariant=1)
c.setTitle('SAM Volume I Chapter III: '+TITLE);c.setAuthor('Sean Brady; OpenAI ChatGPT and Codex')
c.setSubject('Source-bound development,15 October2026')
for n,(left,right) in enumerate(PAGES,1):
 c.setStrokeColor(r.RULE);c.setLineWidth(.5);c.line(41,754,571,754)
 c.setFillColor(r.BLUE);c.setFont('SansBold',7.5);c.drawString(41,765,'SAM / VOLUME I / CHAPTER III')
 c.setFillColor(r.MUTED);c.setFont('Sans',7.5);c.drawRightString(571,765,'DEVELOPMENT / 15 OCTOBER 2026')
 c.line(41,37,571,37);c.setFont('Sans',7.2);c.drawString(41,24,'Brady / ChatGPT / Codex');c.drawRightString(571,24,str(n))
 top=737
 if n==1:
  title=Paragraph('The spherical accumulation kernel<br/>and the source-to-field interface',r.STYLES['title']);_,h=title.wrap(530,100);title.drawOn(c,41,737-h)
  sub=Paragraph('Chapter III / Source-bound development<br/>Sean Brady / Originator and conceptual director<br/>OpenAI ChatGPT and Codex / Research collaborators and co-authors',r.STYLES['sub']);_,sh=sub.wrap(530,70);sub.drawOn(c,41,727-h-sh)
  ab=Paragraph('<b>Abstract.</b> '+r.markup(ABSTRACT),r.STYLES['abstract']);_,ah=ab.wrap(530,140);ab.drawOn(c,41,715-h-sh-ah);top=700-h-sh-ah
 r.frame(c,r.parse(left),41,top,r.CW,51,f'{n} left')
 r.frame(c,r.parse(right),41+r.CW+r.GAP,top,r.CW,51,f'{n} right');c.showPage()
c.save();(HERE/'LAYOUT.json').write_text(json.dumps(r.LAYOUT,indent=2)+'\n')
print(json.dumps(dict(pdf=str(out),pages=len(PAGES),sha256=hashlib.sha256(out.read_bytes()).hexdigest())))
