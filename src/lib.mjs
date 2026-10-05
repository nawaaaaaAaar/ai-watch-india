export const DRAFT_URL = 'https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf';
export const FINAL_URL = 'https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf';
export const ACT_URL = 'https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf';
export const CORRECTION_URL = 'https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf';
export const SGI_FINAL='https://www.meity.gov.in/static/uploads/2026/02/f55fe52418b03f58b0669f6a8bc03b6d.pdf';
export const SGI_CORRECTION='https://www.meity.gov.in/static/uploads/2026/03/20c30107195f68865104dd4e16176f4d.pdf';
export const REPO = 'https://github.com/nawaaaaaAaar/ai-watch-india';
export const ORIGINAL_CONTRIBUTIONS=['rule-8','rule-14','rule-13','schedule-fourth','rule-7','rule-11','schedule-second','rule-1','rule-6','rule-3','rule-15','rule-23'];
export function mergeCollections(original, expansion, implementation, publicServices, context) {
  const families=[{id:'dpdp',title:'Digital Personal Data Protection Rules, 2025',shortTitle:'DPDP Rules',
    status:'Notified rules + corrigenda',description:'Consultation draft to final rules, preserving correction and timing uncertainty.',
    coverage:'All 23 final rules and seven schedules; eight directed English corrections.',count:30,
    contributionCount:12,defaultId:'rule-8',scope:'Complete final-provision inventory, not current court-status or later-amendment certification.',
    timeline:[{date:'03 Jan 2025',title:'Consultation draft',detail:'22 rules and seven schedules'},
      {date:'13 Nov 2025',title:'Notified final',detail:'13/14 Nov publication basis flagged'},
      {date:'10 Dec 2025',title:'Corrigenda',detail:'Eight substitutions; Gazette dated 11 Dec'}]},...expansion.families,...(implementation?.families||[]),...(publicServices?.families||[])];
  return {title:publicServices?'Five Indian policy and public-service evidence collections':implementation?'Four Indian digital-policy evidence collections':'Three Indian digital-policy collections',checked:'DPDP: 4 October 2026; expansion: 5 October 2026',
    families,sources:[...original.sources,...expansion.sources,...(implementation?.sources||[]),...(publicServices?.sources||[]),...(context?.sources||[])],
    provisions:[...original.provisions.map(p=>({...p,familyId:'dpdp',comparisonKind:'Draft to final',contribution:ORIGINAL_CONTRIBUTIONS.includes(p.id)})),...expansion.provisions,...(implementation?.provisions||[]),...(publicServices?.provisions||[])],
    corrections:[...original.corrections.map(c=>({...c,familyId:'dpdp',sourceUrl:CORRECTION_URL})),...expansion.corrections]};
}
export function evidenceLinks(p) {
  return {before:p.draftUrl||`${DRAFT_URL}#page=${p.draftPage}`,
    after:p.finalUrl||`${FINAL_URL}#page=${p.finalPage}`,
    beforeLocator:p.draftLocator||`Draft, p. ${p.draftPage}`,
    afterLocator:p.finalLocator||`Final, p. ${p.finalPage}`};
}
export function filterProvisions(records, query='', type='All', actor='All', family='All') {
  const terms=query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  return records.filter(p => (family==='All'||p.familyId===family)&&(type==='All'||p.type===type)&&(actor==='All'||p.actor===actor)&&
    terms.every(t=>`${p.id} ${p.label} ${p.title} ${p.summary} ${p.interpretation} ${p.actor} ${p.draftLabel} ${p.familyId||''} ${p.question} ${p.caution} ${p.draftText} ${p.finalText} ${JSON.stringify(p.caseFields||[])}`.toLowerCase().includes(t)));
}
export function validateNotebook(raw, validIds) {
  if (!raw || raw.version!==1 || !Array.isArray(raw.selected) || !Array.isArray(raw.reviews) ||
      typeof raw.title!=='string' || raw.title.length>200) throw new Error('Not a supported AI Watch notebook.');
  if(raw.selected.length>validIds.length || new Set(raw.selected).size!==raw.selected.length ||
     !raw.selected.every(id=>validIds.includes(id))) throw new Error('Notebook has invalid or duplicate provision IDs.');
  if(raw.reviews.length>500) throw new Error('Notebook contains too many review events.');
  for(const r of raw.reviews) {
    if(!validIds.includes(r.provisionId)||typeof r.reviewer!=='string'||!r.reviewer.trim()||r.reviewer.length>100||
      typeof r.note!=='string'||r.note.length>4000||!['checked','disputed'].includes(r.status)||
      typeof r.timestamp!=='string'||!Number.isFinite(Date.parse(r.timestamp))) throw new Error('Notebook contains an invalid review event.');
  }
  return {version:1, selected:[...raw.selected], title:raw.title,
    reviews:raw.reviews.map(r=>({provisionId:r.provisionId, reviewer:r.reviewer,note:r.note,status:r.status,timestamp:r.timestamp}))};
}
export function createBrief(data, notebook, date=new Date().toISOString()) {
  const records=notebook.selected.map(id=>data.provisions.find(p=>p.id===id)).filter(Boolean);
  const title=notebook.title.trim()||'Policy change brief';
  let out=`# ${title}\n\nWorking research brief | Exported ${date}\n\nCollection: ${data.title}. Evidence checked ${data.checked}.\n\n`;
  out+='Analyst-reviewed extracted English text, not independent legal review or personalized legal advice. Session checks and notes are user annotations, not public editorial approval. No current court-status or exhaustive later-amendment certification is made.\n\n';
  out+='## Timing and scope\n\n';
  if(records.some(p=>!p.familyId||p.familyId==='dpdp'))out+='DPDP: the official rule specifies publication, one-year and eighteen-month commencement groups. The 13/14 November publication-date basis is unresolved in this collection; computed calendar dates are not presented as settled deadlines. Notified does not mean every duty is operative. See the [official Rules]('+FINAL_URL+') and the [corrigenda]('+CORRECTION_URL+').\n\n';
  if(records.some(p=>p.familyId==='sgi'))out+='Synthetic media: the [amendment]('+SGI_FINAL+') states commencement on 20 February 2026; English citations were [corrected on 26 February]('+SGI_CORRECTION+'). This is not exhaustive current court-status certification. Some comparisons use prior consolidated law because the final change was absent from the consultation draft.\n\n';
  if(records.some(p=>p.familyId==='aig'))out+='AI governance: recommendation lineage, not a one-to-one legal redline. The published guidelines do not themselves enact every recommended mandate, deadline or institution. Later implementation must be separately verified.\n\n';
  if(records.some(p=>p.familyId==='impl'))out+='Implementation evidence: constitution, recruitment, selections, commitments and operational outcomes are different milestones. Status describes the reviewed records, not an audit or proof of absence. Sources were checked on 5 October 2026; no agency confirmation was requested.\n\n';
  if(records.some(p=>p.familyId==='service'))out+='Public-service cases: six bounded investigations, including an explicitly experimental judicial tool. Each preserves twelve accountability dimensions. Official self-reports, vendor accounts, specifications and independent evaluations are distinct evidence categories. Missing records are not proof of absence; no nationwide census, operational audit or agency confirmation is claimed.\n\n';
  for(const p of records) {
    const links=evidenceLinks(p);
    out+=`## ${p.label}: ${p.title}\n\nCollection: ${p.familyId||'dpdp'}. Comparison: ${p.comparisonKind||'Draft to final'}. Type: ${p.type}. Actor/class: ${p.actor}. Earlier context: ${p.draftLabel}.\n\n`;
    if(p.legalStatus)out+=`Status: ${p.legalStatus}.\n\n`;
    out+=`### Textual observation\n\n${p.summary} [${links.beforeLocator}](${links.before}) [${links.afterLocator}](${links.after})\n\n`;
    out+=`Earlier excerpt (${p.beforeLabel||'consultation draft'}, as extracted):\n\n> ${p.beforeExcerpt}\n\nLater excerpt (${p.afterLabel||'final'}, as printed, as extracted):\n\n> ${p.afterExcerpt}\n\n`;
    out+=`### Analyst interpretation\n\n${p.interpretation}\n\n### Limits and follow-up\n\n${p.caution}\n\nReporting question: ${p.question}\n\n`;
    if(p.caseFields)out+='### Complete accountability matrix\n\n'+p.caseFields.map(f=>`#### ${f.name}\n\nEvidence status: ${f.status}.\n\n${f.statement}\n\n`+(f.evidence.length?f.evidence.map(e=>`[${e.title}: ${e.locator}](${e.url})\n\n> ${e.quote}\n`).join('\n'):'No supporting record verified in the documented search scope.\n')).join('\n')+'\n';
    if(p.evidenceTrail)out+=`### ${p.publicServiceCase?'System':'Implementation'} evidence trail\n\n`+p.evidenceTrail.map(e=>`[${e.title}: ${e.locator}](${e.url})\n\n> ${e.quote}\n`).join('\n')+'\n';
    if(p.requestChecklist)out+='### Records to request or verify\n\n'+p.requestChecklist.map(x=>`- ${x}`).join('\n')+'\nThis is a research checklist, not a filed information request or a determination of the appropriate legal procedure.\n\n';
    if(p.correctionIds.length) out+=`Corrections relevant to this provision: ${p.correctionIds.join(', ')}. Check the [official correcting instrument](${p.familyId==='sgi'?SGI_CORRECTION:CORRECTION_URL}) and compare as-printed versus corrected text before quoting.\n\n`;
    if(['rule-5','rule-15','rule-16','rule-23'].includes(p.id)) out+=`Parent statute context: [DPDP Act](${ACT_URL}). Read statutory limits as well as the rule.\n\n`;
    const reviews=notebook.reviews.filter(r=>r.provisionId===p.id);
    if(reviews.length) out+='### Local review history\n\n'+reviews.map(r=>`- ${r.timestamp} | ${r.status} | ${r.reviewer}: ${r.note}`).join('\n')+'\n\n';
  }
  const usedFamilies=new Set(records.map(p=>p.familyId||'dpdp'));
  const usedIds=new Set(records.flatMap(p=>[p.beforeSourceId,p.afterSourceId,...(p.evidenceTrail||[]).map(e=>e.sourceId)]).filter(Boolean));
  const relevantSources=data.sources.filter(s=>usedIds.has(s.id)||(!s.id.startsWith('service-')&&usedFamilies.has(s.id.startsWith('impl-')?'impl':s.id.startsWith('sgi-')?'sgi':s.id.startsWith('aig-')?'aig':'dpdp')));
  out+='## Source provenance\n\n'+relevantSources.map(s=>`- [${s.title}](${s.url}), ${s.instrument}. Document date: ${s.documentDate}. Publication metadata: ${s.publication}. Snapshot integrity: ${s.hashType}; ${s.hash}.`).join('\n')+'\n';
  return out;
}
export function csv(records) {
  const rows=[['ID','Final provision','Earlier counterpart','Title','Type','Actor','Observation','Interpretation','Caution','Earlier URL','Later URL','Collection','Comparison kind','Legal status','Accountability fields (JSON)']];
  for(const p of records){const links=evidenceLinks(p);rows.push([p.id,p.label,p.draftLabel,p.title,p.type,p.actor,p.summary,p.interpretation,p.caution,links.before,links.after,p.familyId||'dpdp',p.comparisonKind||'Draft to final',p.legalStatus||'Notified rules; timing limits apply',JSON.stringify(p.caseFields||[])]);}
  return csvRows(rows);
}
export function accountabilityCsv(records) {
  const rows=[['Case ID','System','Sector','Deployment stage','Dimension','Evidence status','Statement','Evidence URLs','Quoted evidence','Locator','Research limits']];
  for(const p of records)for(const f of p.caseFields||[])rows.push([p.id,p.label,p.sector,p.deploymentStage,f.name,f.status,f.statement,f.evidence.map(e=>e.url).join(' | '),f.evidence.map(e=>e.quote).join(' | '),f.evidence.map(e=>e.locator).join(' | '),p.caution]);
  return csvRows(rows);
}
function csvRows(rows) {
  return rows.map(row=>row.map(value=>{
    let str=String(value);
    if(/^[=+@\-\t\r]/.test(str)) str="'"+str;
    return '"'+str.replaceAll('"','""')+'"';
  }).join(',')).join('\r\n');
}
export function correctionDraft(provision, reason, evidence) {
  return `# Correction proposal: ${provision.label}\n\nProvision ID: ${provision.id}\n\n## Proposed correction\n\n${reason}\n\n## Supporting evidence\n\n${evidence}\n\n## Current observation\n\n${provision.summary}\n\nStatus: proposal only; not submitted and not applied. Review before sharing.\n`;
}
