-- Select all rows from table
SELECT * FROM meal.mytable;

-- select a row from table
SELECT *from meal.mytable limit 1; 

-- select limited rows from table
SELECT *from mytable limit 25;

-- update command
UPDATE mytable 
SET category = "Snacks" where meal_id = 1109;

-- delete command
DELETE from mytable
where meal_id = 1109;

-- insert command
INSERT into mytable 
values(1109, "Snacks","Indian");

-- drop a table
drop table mytable;

-- Sort in an order
SELECT *FROM mytable
ORDER BY cuisine DESC;
