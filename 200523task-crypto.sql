

*/ FINDING THE MAXIMUM INCREASE IN 7 DAYS

CREATE VIEW best_performing_crypto
AS
select Coin, _7d, Mkt_Cap, Column_2 AS rank
from task2
WHERE Column_2 BETWEEN '1' AND'25'


*/ CONVERT 7 DAYS INCREASE TO PERCENTAGE

SELECT CONCAT(_7D, '%')
FROM task2;



*/ PORTFOLIO VALUE AFTER INVESTING 10,000

create table investment (
	coin nvarchar (50),
	qty float , 
	purchase_cost float,
	purchase_date date,
	purchase_price float, 
	current_value float, 
	realized_profit float, 
	change_in_pc float
);


insert into investment (coin, qty, purchase_cost, purchase_date, purchase_price,
			current_value, realized_profit, change_in_pc) 
			values ('BNB', 31.04, 10000, '2023-04-28', 322.07, 325.62, 110.2, 1.102);


create view investment2
as
SELECT *
FROM investment;


*/ FIND THE CHANGE IN PRICE OVER TIME

 ALTER VIEW investment5
 AS
 SELECT
	*
FROM 
	[DA-LON4].[dbo].[bnb_pricechange]
WHERE
	Date BETWEEN '2023-04-25' AND '2023-05-10';


*/ CONVERT TO PERCENTAGE 

SELECT CONCAT(change_in_pc, '%') as new
FROM investment;

