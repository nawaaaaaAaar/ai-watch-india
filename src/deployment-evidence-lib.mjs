export function caseObservations(data,systemId){
 const ids=new Set(data.case_observations.filter(l=>l.system_id===systemId).map(l=>l.observation_id));
 return data.observations.filter(o=>ids.has(o.observation_id));
}
export function filterCases(data,{query='',dimension='All',strength='All'}={}){
 const q=query.trim().toLowerCase();
 return data.cases.filter(c=>{
  const observations=caseObservations(data,c.system_id);
  const filtered=observations.filter(o=>(dimension==='All'||o.dimension===dimension)&&(strength==='All'||o.evidence_strength===strength));
  if(!filtered.length)return false;
  return !q||[c.name,c.jurisdiction,c.sector,c.change_in_understanding,...filtered.map(o=>o.statement)].join(' ').toLowerCase().includes(q);
 });
}
