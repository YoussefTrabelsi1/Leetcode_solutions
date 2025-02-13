WITH ranked_measurements AS (
  SELECT 
    CAST(measurement_time AS Date) AS measurement_day,
    measurement_value,
    ROW_NUMBER() OVER (PARTITION BY CAST(measurement_time AS Date) ORDER BY measurement_time) AS nb
  FROM measurements)
  
SELECT
  measurement_day,
  SUM(CASE WHEN nb % 2 = 1 THEN measurement_value ELSE 0 END) AS odd_sum,
  SUM(CASE WHEN nb % 2 = 0 THEN measurement_value ELSE 0 END) AS even_sum
FROM ranked_measurements
GROUP BY measurement_day