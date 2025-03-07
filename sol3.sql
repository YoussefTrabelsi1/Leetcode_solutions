WITH RECURSIVE all_toppings AS (
-- 1st element: Non-recursive query
SELECT
  topping_name::VARCHAR,
  ingredient_cost::DECIMAL AS total_cost,
  1 AS topping_numbers
FROM pizza_toppings

-- 2nd element: UNION ALL
UNION ALL 

-- 3rd element: Recursive query
SELECT
  CONCAT(addon.topping_name, ',', anchor.topping_name) AS topping_name,
  addon.ingredient_cost + anchor.total_cost AS total_cost,
  topping_numbers + 1
FROM 
  pizza_toppings AS addon, 
  all_toppings AS anchor
WHERE anchor.topping_name < addon.topping_name
)

-- Querying the output
SELECT * 
FROM all_toppings;