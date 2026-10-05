export function filterGovernance(data,{query='',jurisdiction='All',status='All',type='All'}={}){
 const q=query.trim().toLowerCase();
 return data.instruments.filter(i=>(jurisdiction==='All'||i.jurisdiction===jurisdiction)&&(status==='All'||i.document_status===status)&&(type==='All'||i.instrument_type===type)&&(!q||[i.title,i.issuing_body,i.scope,i.jurisdiction,...data.instrument_domains.filter(d=>d.instrument_id===i.instrument_id).map(d=>d.domain)].join(' ').toLowerCase().includes(q)));
}
