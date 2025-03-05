WITH calls_per_holder AS (
  SELECT 
    policy_holder_id,
    COUNT(DISTINCT case_id) AS policy_holder_count
  FROM callers 
  GROUP BY policy_holder_id
  HAVING COUNT(DISTINCT case_id)>2
)

SELECT 
  count(policy_holder_count) AS policy_holder_count
FROM calls_per_holder;