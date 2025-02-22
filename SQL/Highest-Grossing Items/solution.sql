SELECT
  category,
  product,
  total_spend
FROM 
  (SELECT 
    category,
    product,
    SUM(spend) AS total_spend, 
    RANK() OVER (PARTITION BY category ORDER BY SUM(spend) DESC) AS rk
  FROM product_spend
  WHERE EXTRACT (YEAR FROM transaction_date)='2022'
  GROUP BY category,product
  ORDER BY category,total_spend DESC) A
WHERE rk<3;