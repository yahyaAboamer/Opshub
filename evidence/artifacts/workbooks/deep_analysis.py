from inspect_workbooks import *

def rowmatrix(sheet,start=1,end=None):
    end=end or max(int(re.search(r'\d+$',r).group()) for r in sheet['cells'])
    rows=[]
    for r in range(start,end+1):
        nonempty=[{'cell':ref,'value':c['v'],'formula':'='+c['f'] if c['f'] else None} for ref,c in sheet['cells'].items() if int(re.search(r'\d+$',ref).group())==r and (c['v'] is not None or c['f'])]
        if nonempty:rows.append({'row':r,'cells':nonempty})
    return rows

def safe_sheet_profile(s,headerrow=3):
    cells=s['cells']
    headers={colnum(ref):str(c['v']) for ref,c in cells.items() if int(re.search(r'\d+$',ref).group())==headerrow and c['v'] is not None and c['f'] is None}
    bycolumn=collections.defaultdict(list)
    for ref,c in cells.items():bycolumn[colnum(ref)].append((ref,c))
    formulas={}
    for col,h in headers.items():
        cs=[(ref,c) for ref,c in bycolumn[col] if c['f'] is not None]
        if cs:formulas[h]={'column':collabel(col),'formula_count':len(cs),'first_cell':cs[0][0],'example':'='+cs[0][1]['f'],'cached_nonempty_count':sum(c['v'] not in (None,'') for _,c in cs),'cached_empty_count':sum(c['v'] in (None,'') for _,c in cs)}
    rows={}
    first_data_row=4 if s['name']=='DATA_Master' else headerrow+1
    for ref,c in cells.items():
        r=int(re.search(r'\d+$',ref).group())
        if r<first_data_row:continue
        if c['v'] is not None or c['f'] is not None:rows.setdefault(r,{})[colnum(ref)]=c
    counts={}
    for col,h in headers.items():
        vals=[(r,row[col]['v']) for r,row in rows.items() if col in row and row[col]['v'] not in (None,'')]
        vals_no_formula=[(r,v) for r,v in vals if not rows[r][col]['f']]
        count={'column':collabel(col),'nonempty_values':len(vals),'input_nonempty_values':len(vals_no_formula),'distinct_values':len(set(str(v) for r,v in vals)),'numeric_count':sum(isinstance(v,(int,float)) and not isinstance(v,bool) for _,v in vals),'formula_cells':sum(col in row and row[col]['f'] is not None for row in rows.values())}
        if vals_no_formula:count.update({'first_input_row':vals_no_formula[0][0],'last_input_row':vals_no_formula[-1][0]})
        # Only safe enumerations and aggregate numeric fields are retained.
        if re.search(r'status|root.?cause|return.?type|resolution|channel|courier|call.?outcome|shipment.?type|delivery.?type|payment.?method|currency|financial.?status|fulfillment.?status|taxable|requires.?shipping|lineitem.?vendor|cancelled',h,re.I) and not re.search(r'name|email|phone|address|note|reason',h,re.I):
            frequencies=collections.Counter(str(v) for _,v in vals)
            if len(frequencies)<=100:count['safe_value_counts']=dict(frequencies)
        if vals and count['numeric_count']==len(vals) and not re.search(r'id|number|tracking|phone|mobile|order|awb|index|key|serial',h,re.I):
            nums=[v for _,v in vals];count['numeric_summary']={'min':min(nums),'max':max(nums),'sum':sum(nums),'mean':sum(nums)/len(nums)}
        counts[h]=count
    return {'sheet':s['name'],'header_row':headerrow,'first_data_row':first_data_row,'headers':[{'cell':f'{collabel(col)}{headerrow}','label':h} for col,h in headers.items()],'row_count_with_stored_values_or_formulas':len(rows),'columns':counts,'formula_columns':formulas}

def controls(book):
    names=['Config','START','Change_Log','Setup guide','Paste into Lists','Migration formulas','Your weekly paste','READ_ME']
    result={s['name']:rowmatrix(s) for s in book['sheets'] if s['name'] in names}
    # The generated top-up README embeds one customer and an example phone.
    for row in result.get('READ_ME',[]):
        for cell in row['cells']:
            if cell['cell']=='A17':cell['value']=re.sub(r'\d{11,13}','[phone example redacted]',str(cell['value']))
            if cell['cell']=='A21':cell['value']=re.sub(r'\([^)]*\)','(customer identification redacted)',str(cell['value']))
    return result

def make_report(book):
    path=book['path'];stem=path.stem
    (OUT/(stem+'.controls.json')).write_text(json.dumps(controls(book),ensure_ascii=False,indent=2),encoding='utf-8')
    profiles=[]
    for s in book['sheets']:
        if s['name'].startswith('RAW_') or s['name'] in ['DATA_Master','Orders_Master']:
            headerrow=3 if s['name']=='Orders_Master' else (1 if path.name.startswith('2026-') else 2)
            p=safe_sheet_profile(s,headerrow);profiles.append(p)
        elif path.name.startswith('2026-'):
            p=safe_sheet_profile(s,1);profiles.append(p)
    (OUT/(stem+'.data_profiles.json')).write_text(json.dumps(profiles,ensure_ascii=False,indent=2),encoding='utf-8')
    print(stem,[(p['sheet'],len(p['headers']),p['row_count_with_stored_values_or_formulas']) for p in profiles],flush=True)
    return profiles

if __name__=='__main__':
    for path in sorted(SOURCE.glob('*.xlsx')):
        if path.name.startswith('~$'):continue
        print('Deep scanning',path.name,flush=True)
        book=load_book(path);make_report(book);book['zip'].close()
