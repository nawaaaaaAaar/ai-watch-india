-- Run: sqlite3 public/governance/dataset.sqlite < research/governance/queries.sql
-- Counts describe selected documents, not national prevalence or system compliance.
SELECT document_status, COUNT(*) AS document_versions FROM instruments GROUP BY document_status ORDER BY document_status;
SELECT jurisdiction, COUNT(*) AS document_versions FROM instruments GROUP BY jurisdiction ORDER BY jurisdiction;
SELECT i.title,i.document_status,l.link_type,s.name,l.rationale
FROM system_links l JOIN instruments i USING(instrument_id) JOIN system_keys s USING(system_id)
WHERE l.link_type LIKE '%Named%' OR l.link_type LIKE '%Explicit%';
-- A textual redress clause can be draft, contextual or about incentives; inspect summaries.
SELECT i.title,i.document_status,p.presence,p.summary,p.provision_force
FROM provisions p JOIN instruments i USING(instrument_id)
WHERE p.dimension='Redress' AND p.presence='Textual provision';
SELECT i.title,s.name,l.link_type,l.applicability_determination
FROM system_links l JOIN instruments i USING(instrument_id) JOIN system_keys s USING(system_id)
WHERE i.document_status='Draft / consultation';
SELECT i.title,i.jurisdiction,i.document_status FROM instruments i
WHERE NOT EXISTS(SELECT 1 FROM system_links l WHERE l.instrument_id=i.instrument_id);
SELECT i.title,i.operative_status,i.commencement_text FROM instruments i
WHERE i.instrument_family LIKE '%dpdp%' OR i.document_status LIKE 'Historical%';
-- Both halves of a link: policy excerpt and existing registry assertion IDs.
SELECT l.system_link_id,e.quote,e.locator,l.system_assertion_ids,l.system_source_urls
FROM system_links l,json_each(l.instrument_evidence_ids) a
JOIN evidence e ON e.evidence_id=a.value;
