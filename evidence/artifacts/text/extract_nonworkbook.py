"""Read-only OOXML/PDF/source inspection. Never imports or executes source scripts."""
import hashlib, json, re, struct, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(r'D:\Desktop\Opshub\source')
OUT=Path(r'D:\Desktop\Opshub\evidence\artifacts\text')
OUT.mkdir(parents=True,exist_ok=True)
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def scrub(t):
    t=re.sub(r'\b(?:\+?20)?0?1[0125][\s-]?\d[\d\s-]{7,}\b','[PHONE REDACTED]',t)
    t=re.sub(r'\b\d{7,}\b','[IDENTIFIER REDACTED]',t)
    t=re.sub(r'#\d{4,}','[ORDER REF REDACTED]',t)
    t=re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}','[EMAIL REDACTED]',t)
    return t

items=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix.lower() in ('.xlsx','.csv'): continue
    rel=str(p.relative_to(ROOT)).replace('\\','/')
    obj={'file':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    if p.suffix.lower()=='.docx':
        with zipfile.ZipFile(p) as z:
            x=ET.fromstring(z.read('word/document.xml'))
            body=x.find(W+'body'); blocks=[]; paraidx=0; tableidx=0
            for ch in body:
                if ch.tag==W+'p':
                    paraidx+=1; t=''.join(ch.itertext()) if False else ''.join(ch.itertext())
                    t=''.join(e.text or '' for e in ch.iter(W+'t'))
                    sty=ch.find(W+'pPr/'+W+'pStyle')
                    blocks.append({'locator':f'P{paraidx}','style':sty.attrib.get(W+'val','') if sty is not None else '', 'text':scrub(t)})
                elif ch.tag==W+'tbl':
                    tableidx+=1; rows=[]
                    for ri,row in enumerate(ch.findall(W+'tr'),1):
                        cells=[' | '.join(''.join(e.text or '' for e in pp.iter(W+'t')) for pp in cell.findall(W+'p')) for cell in row.findall(W+'tc')]
                        rows.append({'locator':f'T{tableidx}R{ri}','cells':[scrub(v) for v in cells]})
                    blocks.append({'locator':f'T{tableidx}','rows':rows})
            obj.update(paragraphs=paraidx,tables=tableidx,embedded_images=sum(v.startswith('word/media/') for v in z.namelist()),tracked_insertions=len(x.findall('.//'+W+'ins')),tracked_deletions=len(x.findall('.//'+W+'del')),has_comments='word/comments.xml' in z.namelist())
            if 'docProps/core.xml' in z.namelist():
                c=ET.fromstring(z.read('docProps/core.xml'))
                obj['core_properties']={el.tag.split('}')[-1]:scrub(el.text or '') for el in c}
            # Reports use deliberately aggregate output; all table data is inspected after identifier redaction.
            (OUT/(p.stem+'.blocks.json')).write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
            lines=[]
            for b in blocks:
                if 'text' in b: lines.append(b['locator']+' ['+b['style']+'] '+b['text'])
                else:
                    for r in b['rows']: lines.append(r['locator']+' '+ ' || '.join(r['cells']))
            (OUT/(p.stem+'.extracted.txt')).write_text('\n'.join(lines),encoding='utf-8')
    elif p.suffix.lower()=='.pdf':
        import pdfplumber
        with pdfplumber.open(p) as pdf:
            obj['pages']=len(pdf.pages)
            pages=[]
            for i,page in enumerate(pdf.pages,1): pages.append({'page':i,'text':scrub(page.extract_text() or ''),'tables':[[[scrub(v or '') for v in row] for row in tbl] for tbl in page.extract_tables()]})
            (OUT/(p.stem+'.pdf-text.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
    elif p.suffix.lower()=='.pyc':
        raw=p.read_bytes(); flags=int.from_bytes(raw[4:8],'little')
        obj['pyc']={'magic_hex':raw[:4].hex(),'flags':flags,'timestamp':int.from_bytes(raw[8:12],'little') if flags==0 else None,'source_size':int.from_bytes(raw[12:16],'little') if flags==0 else None,'header_only_inspection':True}
    else:
        txt=p.read_text(encoding='utf-8-sig'); obj['lines']=len(txt.splitlines())
        # Do not duplicate original scripts/specs; source file + stable line references serve as evidence.
    items.append(obj)
(OUT/'nonworkbook-manifest.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'artifacts':len(items),'output_files':len(list(OUT.iterdir())),'docx':[{'file':x['file'],'paragraphs':x['paragraphs'],'tables':x['tables'],'images':x['embedded_images']} for x in items if 'paragraphs' in x],'pdf':[{'file':x['file'],'pages':x['pages']} for x in items if 'pages' in x]},indent=2))
