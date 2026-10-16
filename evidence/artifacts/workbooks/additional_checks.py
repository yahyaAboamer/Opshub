from reconcile_workbooks import *

def shape_overflow(path):
    z=zipfile.ZipFile(path);wb=ET.fromstring(z.read('xl/workbook.xml'));rels={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))};result=[]
    for sh in wb.findall('m:sheets/m:sheet',NS):
        target=rels[sh.get(RNS+'id')];xmlpath=target.lstrip('/') if target.startswith('/') else 'xl/'+target;r=ET.fromstring(z.read(xmlpath));dim=r.find('m:dimension',NS)
        if dim is None:continue
        end=dim.get('ref').split(':')[-1];dc=colnum(end);dr=int(re.search(r'\d+$',end).group());active=[c.get('r') for c in r.findall('m:sheetData/m:row/m:c',NS) if c.find('m:v',NS) is not None or c.find('m:is',NS) is not None or c.find('m:f',NS) is not None]
        actualc=max([colnum(a) for a in active] or [0]);actualr=max([int(re.search(r'\d+$',a).group()) for a in active] or [0]);outside=[a for a in active if colnum(a)>dc or int(re.search(r'\d+$',a).group())>dr]
        if outside:result.append({'sheet':sh.get('name'),'declared_dimension':dim.get('ref'),'actual_max_column':collabel(actualc),'actual_max_row':actualr,'cells_outside_declared_dimension':len(outside)})
    z.close();return result

def rowseq(sh,first=3,key=1):
    out=collections.defaultdict(list)
    for r,row in key_records(sh,key,first):out[clean(row.get(key))].append(row)
    return out

def sequence_compare(a,b,width=79,firsta=3,firstb=2):
    aa,bb=rowseq(a,firsta),rowseq(b,firstb);common=set(aa)&set(bb);mismatches=collections.Counter();changedorders=set();countmismatch=0
    for key in common:
        if len(aa[key])!=len(bb[key]):countmismatch+=1;changedorders.add(key)
        for ra,rb in zip(aa[key],bb[key]):
            for i in range(1,width+1):
                if not value_equal(ra.get(i),rb.get(i)):mismatches[collabel(i)]+=1;changedorders.add(key)
    return {'common_order_keys':len(common),'left_matched_line_rows':sum(len(aa[k]) for k in common),'right_matched_line_rows':sum(len(bb[k]) for k in common),'orders_with_different_line_row_counts':countmismatch,'orders_with_any_field_difference':len(changedorders),'differing_cells_by_column':dict(mismatches),'method':'Exact order reference match; compare all line rows per matched reference in retained within-order sequence across export columns A:CA, excluding helper CB:CC. Decimal text and number representations normalized for field comparison only.'}

if __name__=='__main__':
    curfile='02_Gentry_Delivery_Performance_System.xlsx';cur=selected_book(SOURCE/curfile,['Config','RAW_Bosta','RAW_Costs','RAW_Intake','RAW_SKU','RAW_Shopify']);current,masters,orders=reconstruct(cur)
    v2=selected_book(SOURCE/'02_Gentry_Delivery_Performance_System_v2.0_BACKUP_2026-08-28.xlsx',['Config','RAW_Bosta','RAW_Costs','RAW_Intake','RAW_SKU']);v2calc,vm,vo=reconstruct(v2)
    verify={'C34':v2calc['aov_delivered_positive_cod'],'C36':v2calc['aov_delivered_positive_cod'],'C37':v2calc['blended_cogs_pct'],'C38':v2calc['gross_margin_pct'],'C40':v2calc['saved_return_margin_proxy'],'C166':v2calc['shipments'],'C167':v2calc['channels'].get('Outbound',0),'C168':v2calc['status_groups'].get('Delivered',0),'C169':v2calc['status_groups'].get('Returned',0),'C170':0,'C171':v2calc['status_groups'].get('Customer return',0),'C172':v2calc['status_groups'].get('Exchange return',0)}
    cacheverify=[{'cell':'Config!'+ref,'cached':v2['Config']['cells'].get(ref),'independent_reconstruction':value,'agree_within_1e-9':numeric(v2['Config']['cells'].get(ref)) and abs(v2['Config']['cells'][ref]-value)<=1e-9} for ref,value in verify.items()]
    stage=selected_book(SOURCE/'2026-09-08_RAW_Shopify_STAGED_18Jun-08Sep.xlsx',['RAW_Shopify_PASTE'])['RAW_Shopify_PASTE'];stagecomp=sequence_compare(cur['RAW_Shopify'],stage)
    v3=selected_book(SOURCE/'02_Gentry_Delivery_Performance_System_v3.0_BACKUP_2026-09-08.xlsx',['RAW_Shopify'])['RAW_Shopify'];cp,crows=csv_profile(SOURCE/'2026-08-28_Shopify_orders_18Jun-17Aug.csv');csh={'name':'source_csv','rows':{i+2:{j+1:r.get(h) for j,h in enumerate(cp['headers'])} for i,r in enumerate(crows)}};csvcomp=sequence_compare(v3,csh)
    topup=selected_book(SOURCE/'2026-09-08_Hadeer_CallQueue_TopUp_27rows.xlsx',['PASTE_AT_A102'])['PASTE_AT_A102'];topids={clean(row.get(4)) for r,row in key_records(topup,4,2)};bm={m['id']:m for m in masters}
    parserdifferences=[];missingbyslot=collections.Counter();truncation=[]
    for r,row in key_records(cur['RAW_Bosta'],1,3):
        desc=str(row.get(22) or '');actual=[xtrim(line) for line in desc.split('\n')][:4];window=[xtrim(desc.replace('\n',' '*180)[i*180:(i+1)*180]) for i in range(4)]
        if actual+['']*(4-len(actual))!=window:parserdifferences.append(r)
        if any(len(line)>180 for line in actual):truncation.append(r)
    groupmismatch=sum(m['state']!='Delivered' and m['group']=='Delivered' for m in masters)
    out={'v2_cached_formula_crosscheck':cacheverify,'source_csv_vs_v3_complete_line_sequences':csvcomp,'staged_shopify_vs_current_complete_line_sequences':stagecomp,'declared_dimension_overflows':{f:shape_overflow(SOURCE/f) for f in [curfile,'02_Gentry_Delivery_Performance_System_v3.0_BACKUP_2026-09-08.xlsx']},'current_capacities':{'raw_shopify_helper_formula_rows':5000,'raw_shopify_named_source_rows':'3:5002','actual_line_rows':2082,'actual_order_header_rows':1635,'orders_master_formula_slots':2000,'orders_represented':len(orders),'order_overflow_count':max(0,1635-2000),'data_master_formula_slots':2000,'bosta_records':569,'cost_named_range_rows':'3:2002','cost_records':1381,'costs_outside_named_range_count':0},'topup_verification':{'tracking_ids':len(topids),'matched_current_bosta_ids':len(topids&set(bm)),'type_counts':counts(bm[k]['type'] for k in topids&set(bm)),'created_dates':date_stats(bm[k]['created'] for k in topids&set(bm)),'existing_intake_matches':len(topids&set(clean(row.get(4)) for r,row in key_records(cur['RAW_Intake'],4,3)))},'product_parser_current_sample':{'fixed_180_character_window_differs_from_true_line_split_shipments':len(parserdifferences),'source_rows_where_different':parserdifferences,'any_product_line_over_180_characters_shipments':len(truncation),'observed_non_delivered_states_classified_delivered':groupmismatch},'unapproved_or_untested_formula_edges':['Group I uses SEARCH(deliver,state), so an Out for delivery string would become Delivered; not observed in these Bosta exports.','Only four fixed-width 180-character description windows are read. Data_flags checks SKU missing only slots 1 and 2, even though value calculation accepts four slots.','Positive wallet sum required for wallet source. A recorded zero or negative net fee would fall back to dormant rate card instead of being labelled actual wallet.','Order outcome R prioritizes any Returned to origin leg over any Delivered leg, without restricting leg type or ordering events.','Confirmation SEARCH tags uses substring matching; Hadeer and automatic confirmation are merged in artifact.' ]}
    (OUT/'additional_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(out,ensure_ascii=False,indent=2))
