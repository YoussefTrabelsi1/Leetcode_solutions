WITH RECURSIVE all_toppings AS (
  SELECT
  topping_name::VARCHAR,
  ingredient_cost::DECIMAL AS total_cost,
  1 AS topping_numbers
FROM pizza_toppings

UNION ALL

SELECT
  CONCAT(addon.topping_name, ',', anchor.topping_name) AS topping_name,
  addon.ingredient_cost + anchor.total_cost AS total_cost,
  topping_numbers + 1
FROM 
  pizza_toppings AS addon, 
  all_toppings AS anchor
WHERE anchor.topping_name < addon.topping_name
)

SELECT
  STRING_AGG (single_topping, ',' ORDER BY single_topping) AS pizza,
  total_cost
FROM 
  all_toppings, 
  REGEXP_SPLIT_TO_TABLE(topping_name, ',') AS single_topping
WHERE topping_numbers = 3
GROUP BY topping_name, total_cost
ORDER BY total_cost DESC, pizza;