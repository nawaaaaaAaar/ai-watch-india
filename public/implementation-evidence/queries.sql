-- Run with sqlite3 public/implementation-evidence/dataset.sqlite < research/implementation-evidence/queries.sql
-- The case denominator is 10, not the 144 bridge keys.
SELECT evidence_strength, COUNT(*) AS observations
FROM observations GROUP BY evidence_strength ORDER BY evidence_strength;

SELECT c.name, cv.dimension, cv.evidence_status, cv.unknown_or_next_record
FROM coverage cv JOIN cases c USING(system_id)
WHERE cv.observation_ids='[]' ORDER BY c.name,cv.dimension;

SELECT c.name,o.dimension,o.claim_type,o.statement,d.url
FROM case_observations l JOIN cases c USING(system_id)
JOIN observations o USING(observation_id) JOIN documents d USING(document_id)
WHERE o.dimension IN ('Procurement','Human oversight','Operational status')
ORDER BY c.name,o.observation_id;

SELECT f.amount_kind,f.amount_text,f.actual_spending_verified,d.url
FROM financial_observations f JOIN observations o USING(observation_id)
JOIN documents d USING(document_id);

SELECT p.party_name_text,p.role_text,o.evidence_strength,d.url
FROM party_observations p JOIN observations o USING(observation_id)
JOIN documents d USING(document_id) WHERE o.dimension='Supplier';

SELECT c.name,g.title,l.link_type,l.applicability_determination
FROM governance_links l JOIN cases c USING(system_id)
JOIN governance_keys g USING(instrument_id);

-- Deduplicate shared CAG observations rather than treating links as separate evidence.
SELECT COUNT(DISTINCT observation_id) AS observations,COUNT(*) AS system_links
FROM case_observations WHERE system_id IN ('sys-cag-paras','sys-cag-parakh');
