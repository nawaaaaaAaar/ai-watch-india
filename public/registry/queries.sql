-- Run: sqlite3 public/registry/dataset.sqlite < research/registry/queries.sql
-- These are selected-corpus descriptions, not national prevalence estimates.

-- Source trail for every documented/partial statement in the e-Paarvai case.
SELECT a.field, a.evidence_status, a.value, e.quote, s.title, s.url,
       s.published_date, s.source_type
FROM assertions a
JOIN evidence_links l ON l.record_type='assertions' AND l.record_id=a.assertion_id
JOIN evidence e ON e.evidence_id=l.evidence_id
JOIN sources s ON s.source_id=e.source_id
WHERE a.system_id='sys-epaarvai'
ORDER BY a.assertion_id, s.source_id;

-- Avoid interpreting specification thresholds or usage as measured accuracy.
SELECT y.name, m.metric_name, m.value, m.value_qualifier, m.unit,
       m.metric_kind, m.measurement_scope, m.denominator
FROM metrics m JOIN systems y USING(system_id)
ORDER BY y.name, m.metric_kind, m.metric_name;

-- Allocation is not expenditure or an executed supplier award.
SELECT y.name, p.record_type, p.amount_inr, p.amount_type,
       p.award_date, p.supplier_name, p.current_deployment_link
FROM procurements p JOIN systems y USING(system_id);

-- Explicit unverified redress fields, not proof that no remedy exists.
SELECT y.name, a.value
FROM assertions a JOIN systems y USING(system_id)
WHERE a.field='Complaints & appeal' AND a.evidence_status='Not verified';

-- Distinct system count; never count evidence links as deployments.
SELECT ai_class, COUNT(DISTINCT system_id) AS selected_systems
FROM systems GROUP BY ai_class;

-- Fixed coverage frame; documentary association, not administrative ownership.
SELECT f.institution_name, COUNT(DISTINCT c.system_id) AS included_records,
       f.coverage_status
FROM institution_coverage f
LEFT JOIN coverage_systems c USING(frame_id)
GROUP BY f.frame_id;

-- Fresh source availability is distinct from cached original extraction.
SELECT s.title, r.status, r.matched_excerpts, r.total_excerpts,
       r.cached_retry_matches, r.cached_retry_basis
FROM source_rechecks r JOIN sources s USING(source_id)
ORDER BY r.status, s.title;

-- Do not combine clinical deployments and evaluation infrastructure.
SELECT system_kind, COUNT(*) FROM systems GROUP BY system_kind;
