export const DRAFT_URL = 'https://www.meity.gov.in/static/uploads/2025/02/f8a8e97a91091543fe19139cac7514a1.pdf';
export const FINAL_URL = 'https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf';
export const ACT_URL = 'https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf';
export const CORRECTION_URL = 'https://www.meity.gov.in/static/uploads/2025/12/3c7ebbae0e5456f493f486e6845df86b.pdf';
export const REPO = 'https://github.com/nawaaaaaAaar/ai-watch-india';
export function filterProvisions(records, query='', type='All', actor='All') {
  const terms=query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  return records.filter(p => (type==='All'||p.type===type) && (actor==='All'||p.actor===actor) &&
    terms.every(t=>`${p.label} ${p.title} ${p.summary} ${p.interpretation} ${p.actor} ${p.draftLabel}`.toLowerCase().includes(t)));
}
export function validateNotebook(raw, validIds) {
  if (!raw || raw.version!==1 || !Array.isArray(raw.selected) || !Array.isArray(raw.reviews) ||
      typeof raw.title!=='string' || raw.title.length>200) throw new Error('Not a supported AI Watch India notebook.');
  if(raw.selected.length>30 || new Set(raw.selected).size!==raw.selected.length ||
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
  out+='## Timing and scope\n\nThe official rule specifies publication, one-year and eighteen-month commencement groups. The 13/14 November publication-date basis is unresolved in this collection; computed calendar dates are not presented as settled deadlines. Notified does not mean every duty is operative. See the [official Rules]('+FINAL_URL+') and the [corrigenda]('+CORRECTION_URL+').\n\n';
  for(const p of records) {
    out+=`## ${p.label}: ${p.title}\n\nType: ${p.type}. Actor/class: ${p.actor}. Draft counterpart: ${p.draftLabel}.\n\n`;
    out+=`### Textual observation\n\n${p.summary} [Draft, p. ${p.draftPage}](${DRAFT_URL}#page=${p.draftPage}) [Final, p. ${p.finalPage}](${FINAL_URL}#page=${p.finalPage})\n\n`;
    out+=`Draft excerpt (as extracted):\n\n> ${p.beforeExcerpt}\n\nFinal excerpt (as printed, as extracted):\n\n> ${p.afterExcerpt}\n\n`;
    out+=`### Analyst interpretation\n\n${p.interpretation}\n\n### Limits and follow-up\n\n${p.caution}\n\nReporting question: ${p.question}\n\n`;
    if(p.correctionIds.length) out+=`Corrections relevant to this provision: ${p.correctionIds.join(', ')}. Check the [official correcting instrument](${CORRECTION_URL}) and compare as-printed versus corrected text before quoting.\n\n`;
    if(['rule-5','rule-15','rule-16','rule-23'].includes(p.id)) out+=`Parent statute context: [DPDP Act](${ACT_URL}). Read statutory limits as well as the rule.\n\n`;
    const reviews=notebook.reviews.filter(r=>r.provisionId===p.id);
    if(reviews.length) out+='### Local review history\n\n'+reviews.map(r=>`- ${r.timestamp} | ${r.status} | ${r.reviewer}: ${r.note}`).join('\n')+'\n\n';
  }
  out+='## Source provenance\n\n'+data.sources.map(s=>`- [${s.title}](${s.url}), ${s.instrument}. Document date: ${s.documentDate}. Publication metadata: ${s.publication}. Snapshot integrity: ${s.hashType}; ${s.hash}.`).join('\n')+'\n';
  return out;
}
export function csv(records) {
  const rows=[['ID','Final provision','Draft counterpart','Title','Type','Actor','Observation','Interpretation','Caution','Draft URL','Final URL']];
  for(const p of records) rows.push([p.id,p.label,p.draftLabel,p.title,p.type,p.actor,p.summary,p.interpretation,p.caution,DRAFT_URL,FINAL_URL]);
  return rows.map(row=>row.map(value=>{
    let str=String(value);
    if(/^[=+@\-\t\r]/.test(str)) str="'"+str;
    return '"'+str.replaceAll('"','""')+'"';
  }).join(',')).join('\r\n');
}
export function correctionDraft(provision, reason, evidence) {
  return `# Correction proposal: ${provision.label}\n\nProvision ID: ${provision.id}\n\n## Proposed correction\n\n${reason}\n\n## Supporting evidence\n\n${evidence}\n\n## Current observation\n\n${provision.summary}\n\nStatus: proposal only; not submitted and not applied. Review before sharing.\n`;
}
