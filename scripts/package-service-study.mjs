import {readFileSync,writeFileSync} from 'node:fs';
const root=new URL('../',import.meta.url);
const data=JSON.parse(readFileSync(new URL('src/data/public-services.json',root)));
let out=readFileSync(new URL('research/public-service-study-introduction.md',root),'utf8')+'\n\n## Complete six-case accountability register\n\n';
for(const p of data.provisions){
  out+=`### ${p.label}\n\nSector: ${p.sector}. Deployment evidence: ${p.deploymentStage}. Checked ${p.checked}.\n\n`;
  out+=p.summary+' '+p.evidenceTrail.map(e=>`[${e.title}](${e.url})`).filter((x,i,a)=>a.indexOf(x)===i).join(' ')+'\n\n';
  out+='Analyst interpretation: '+p.interpretation+'\n\nLimits: '+p.caution+'\n\n';
  for(const f of p.caseFields){
    out+=`#### ${f.name}\n\nEvidence status: ${f.status}.\n\n${f.statement}`;
    if(f.evidence.length)out+=' '+f.evidence.map(e=>`[${e.title}: ${e.locator}](${e.url})`).join(' ');
    out+='\n\n';
    for(const e of f.evidence)out+=`> ${e.quote}\n\n[Quoted record: ${e.locator}](${e.url})\n\n`;
    if(!f.evidence.length)out+='No supporting record was verified in the documented search scope. This is a bounded unknown, not proof of absence.\n\n';
  }
  out+='#### Priority records to verify\n\n'+p.requestChecklist.map(x=>`- ${x}`).join('\n')+'\n\nA research checklist, not a filed request or legal-procedure determination.\n\n';
}
out+='## Selected-source inventory\n\n';
for(const s of data.sources)out+=`- [${s.title}](${s.url}): ${s.sourceType}; document/publication date ${s.documentDate}; checked ${s.checked}. Snapshot: ${s.snapshotKind}; ${s.hashType}: \`${s.hash}\`.\n`;
writeFileSync(new URL('public/research/public-service-study.md',root),out);
console.log('Packaged full six-case study and all 72 dimension entries.');
