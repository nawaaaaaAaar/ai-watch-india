export function filterSystems(data,{query='',sector='All',stage='All',ai='All',frame='All',cohort='All',sort='name'}={}) {
  const terms=query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const rows=data.systems.filter(s=>(cohort==='All'||s.research_round===cohort)&&(frame==='All'||(frame==='Outside frame'?!s.frame_id:s.frame_id===frame))&&(sector==='All'||s.sector===sector)&&(stage==='All'||s.stage===stage)&&(ai==='All'||s.ai_class===ai)&&terms.every(t=>{
    const owner=data.institutions.find(i=>i.institution_id===s.owner_institution_id)?.name||'';
    const assertions=data.assertions.filter(a=>a.system_id===s.system_id).map(a=>a.value).join(' ');
    return `${s.name} ${s.system_id} ${owner} ${s.sector} ${s.jurisdiction} ${s.stage} ${s.ai_basis} ${assertions}`.toLowerCase().includes(t);
  }));
  return rows.sort((a,b)=>sort==='date'?(b.latest_record_date||'').localeCompare(a.latest_record_date||'')||a.name.localeCompare(b.name):a.name.localeCompare(b.name));
}
export function registryCsv(data,rows) {
  const cols=['system_id','name','responsible_institution','sector','jurisdiction','stage','latest_record_date','ai_class','ai_basis','checked_date','unit','selection','research_round','system_kind','frame_id','dossier'];
  const cell=v=>{let s=v==null?'':String(v);if(/^[=+\-@\t\r]/.test(s))s="'"+s;return '"'+s.replaceAll('"','""')+'"';};
  return [cols.map(cell).join(','),...rows.map(s=>cols.map(k=>cell(k==='responsible_institution'?data.institutions.find(i=>i.institution_id===s.owner_institution_id)?.name:k==='dossier'?`dossiers/${s.system_id}.md`:s[k])).join(','))].join('\r\n')+'\r\n';
}
export function recordEvidence(data,table,id) {
  return data.evidence_links.filter(l=>l.record_type===table&&l.record_id===id).map(l=>data.evidence.find(e=>e.evidence_id===l.evidence_id)).filter(Boolean).map(e=>({...e,source:data.sources.find(s=>s.source_id===e.source_id)}));
}
