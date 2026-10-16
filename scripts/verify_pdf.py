#!/usr/bin/env python3
"""Verify Chapter II pagination, sections, fonts and reviewed PDF identity."""
from pathlib import Path
import argparse
import hashlib
import json
import re
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]

def verify(pdf):
    reference=ROOT/'manuscript/Chapter_II.pdf'
    reader=PdfReader(pdf)
    if reader.is_encrypted or len(reader.pages)!=24:raise ValueError('Expected unencrypted24-page Chapter II')
    if pdf.read_bytes()!=reference.read_bytes():raise ValueError('PDF bytes differ from reviewed edition')
    text='\n'.join(page.extract_text() for page in reader.pages)
    if any(not re.search(r'\b'+str(n)+r'\.\s',text) for n in range(1,49)):
        raise ValueError('A retained section is missing')
    if '\ufffd' in text:raise ValueError('Missing text glyph')
    font_checks=0
    for page in reader.pages:
        if tuple(map(float,page.mediabox))!=(0,0,612,792):raise ValueError('Unexpected page dimensions')
        for value in page['/Resources']['/Font'].get_object().values():
            font=value.get_object();descriptor=font.get('/FontDescriptor')
            if descriptor:
                if not any(key in descriptor.get_object() for key in ['/FontFile','/FontFile2','/FontFile3']):
                    raise ValueError('Unembedded font')
                font_checks+=1
    return dict(status='PASS',pages=24,sections=48,embedded_font_checks=font_checks,
        byte_identical_to_reviewed=True,sha256=hashlib.sha256(pdf.read_bytes()).hexdigest())

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('pdf',type=Path)
    args=parser.parse_args()
    try:print(json.dumps(verify(args.pdf.resolve()),indent=2));return 0
    except (OSError,ValueError,KeyError) as error:
        print(json.dumps(dict(status='FAIL',error=str(error))));return 1

if __name__=='__main__':raise SystemExit(main())
