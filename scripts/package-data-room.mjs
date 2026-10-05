import {readFileSync,writeFileSync,mkdirSync,copyFileSync} from 'node:fs';
import {createBrief,csv,evidenceLinks} from '../src/lib.mjs';
const root=new URL('../',import.meta.url), pub=new URL('public/',root);
const data=JSON.parse(readFileSync(new URL('combined-data.json',pub)));
const dir=new URL('data-room/',pub);mkdirSync(dir,{recursive:true});mkdirSync(new URL('dossiers/',dir),{recursive:true});
const flat=(rows)=>rows.map(row=>row.map(v=>{let x=String(v??'');if(/^[=+@\-\t\r]/.test(x))x="'"+x;return '"'+x.replaceAll('"','""')+'"'}).join(',')).join('\r\n');
const sourceFor=url=>data.sources.find(s=>s.url.split('#')[0]===url.split('#')[0]);
const recordSources=p=>[...new Set([p.beforeSourceId,p.afterSourceId,...(p.evidenceTrail||[]).map(e=>e.sourceId),sourceFor(evidenceLinks(p).before)?.id,sourceFor(evidenceLinks(p).after)?.id].filter(Boolean))];
const evidence=[],coverage=[],gaps=[],all=[];
for(const p of data.provisions){
  const ids=recordSources(p),links=evidenceLinks(p);
  let text=createBrief(data,{version:1,title:`Record dossier: ${p.label}`,selected:[p.id],reviews:[]},'5 October 2026');
  text+='\n## All stored record fields\n\nThese are the curated record fields, not a complete original instrument or a live-system audit. The quoted text segments are those stored by this collection; open the original for wider context.\n\n```json\n'+JSON.stringify(p,null,2)+'\n```\n';
  writeFileSync(new URL(`dossiers/${p.id}.md`,dir),text);all.push(text);
  coverage.push({id:p.id,family:p.familyId,label:p.label,title:p.title,kind:p.type,contribution:!!p.contribution,
    sourceIds:ids,sourceCount:ids.length,accountabilityDimensions:p.caseFields?.length||0,
    dossier:`data-room/dossiers/${p.id}.md`,scope:p.evidenceScope||data.families.find(f=>f.id===p.familyId).scope});
  const trail=p.evidenceTrail||[
    {sourceId:sourceFor(links.before)?.id,url:links.before,title:p.beforeLabel||'Earlier source',locator:links.beforeLocator,quote:p.beforeExcerpt},
    {sourceId:sourceFor(links.after)?.id,url:links.after,title:p.afterLabel||'Later source',locator:links.afterLocator,quote:p.afterExcerpt}];
  for(const [i,e] of trail.entries())evidence.push({id:`${p.id}-evidence-${i}`,recordId:p.id,family:p.familyId,...e});
  gaps.push({id:p.id+'-limit',recordId:p.id,family:p.familyId,label:p.label,kind:'Record limit',dimension:'Scope and interpretation',status:'Limit retained',statement:p.caution,sourceUrls:trail.map(e=>e.url),requestChecklist:p.requestChecklist||[]});
  for(const [i,f] of (p.caseFields||[]).entries())if(f.status!=='Documented')gaps.push({id:p.id+'-field-'+i,recordId:p.id,family:p.familyId,label:p.label,kind:'Accountability gap',dimension:f.name,status:f.status,statement:f.statement,sourceUrls:f.evidence.map(e=>e.url),requestChecklist:p.requestChecklist||[]});
  if(p.implementationCheckpoint)gaps.push({id:p.id+'-queue',recordId:p.id,family:p.familyId,label:p.label,kind:'Implementation record queue',dimension:'Records to verify',status:p.evidenceStatus,statement:p.question,sourceUrls:trail.map(e=>e.url),requestChecklist:p.requestChecklist});
}
const assets=[
 ['all-record-dossiers.md','# AI Watch India: All Seventy-Two Record Dossiers\n\nAll stored records, not 72 claims of substantive novelty. The contribution index remains 46 selected briefs. No private notebook notes are included.\n\n'+all.join('\n\n---\n\n')],
 ['records.jsonl',data.provisions.map(p=>JSON.stringify(p)).join('\n')+'\n'],
 ['records.csv',csv(data.provisions)],
 ['coverage.csv',flat([['Record ID','Collection','Label','Title','Kind','Selected contribution','Source IDs','Dimensions','Dossier','Scope'],...coverage.map(p=>[p.id,p.family,p.label,p.title,p.kind,p.contribution,p.sourceIds.join(' | '),p.accountabilityDimensions,p.dossier,p.scope])])],
 ['sources.csv',flat([['Source ID','Title','Source type','Date','Publication basis','Source check','Status','URL','Snapshot','Snapshot kind','Hash type','SHA-256'],...data.sources.map(s=>[s.id,s.title,s.sourceType||s.status,s.documentDate,s.publication,s.checked,s.status,s.url,s.snapshot,s.snapshotKind||'Extracted source text',s.hashType,s.hash])])],
 ['corrections.csv',flat([['ID','Record','Collection','Locator','Original','Directed replacement','Note','Source URL'],...data.corrections.map(c=>[c.id,c.provisionId,c.familyId,c.locator,c.before,c.after,c.note,c.sourceUrl])])],
 ['evidence-items.csv',flat([['Evidence ID','Record','Collection','Source ID','Source title','Locator','Exact stored quote','URL'],...evidence.map(e=>[e.id,e.recordId,e.family,e.sourceId,e.title,e.locator,e.quote,e.url])])],
 ['gaps.csv',flat([['Gap ID','Record','Collection','Label','Kind','Dimension','Status','Statement','Supporting URLs','Records to verify'],...gaps.map(g=>[g.id,g.recordId,g.family,g.label,g.kind,g.dimension,g.status,g.statement,g.sourceUrls.join(' | '),g.requestChecklist.join(' | ')])])],
 ['coverage.json',JSON.stringify(coverage,null,2)+'\n'],['gaps.json',JSON.stringify(gaps,null,2)+'\n'],
 ['evidence-items.json',JSON.stringify(evidence,null,2)+'\n']
];
for(const [name,text] of assets)writeFileSync(new URL(name,dir),text);
for(const file of ['provision-comparison.jsonl','provision-coverage.csv'])copyFileSync(new URL('research/'+file,root),new URL('raw-'+file,dir));
writeFileSync(new URL('dataset-summary.json',dir),JSON.stringify({checked:data.checked,records:coverage,sources:data.sources,gaps,counts:{families:data.families.length,records:data.provisions.length,briefs:data.provisions.filter(p=>p.contribution).length,sources:data.sources.length,corrections:data.corrections.length,accountabilityFields:data.provisions.reduce((n,p)=>n+(p.caseFields?.length||0),0),evidenceItems:evidence.length,gapRows:gaps.length}},null,2)+'\n');
console.log(`Packaged ${coverage.length} full record dossiers, ${evidence.length} evidence items and ${gaps.length} limits/gap rows.`);
