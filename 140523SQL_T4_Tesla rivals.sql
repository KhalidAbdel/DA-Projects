

/*CHECK FOR DUPLICATES

SELECT car_name, COUNT(*) AS count
FROM t4
GROUP BY car_name
HAVING COUNT(*) > 1;


/* FIND ALL TESLA MODELS

create view tesla1705
As
SELECT car_name, price1, max_range, top_speed
FROM t4_newtable
WHERE 
	car_name LIKE '%Tesla%'

/*
*/ WHICH CAR CAN RIVAL TESLA IN TERMS OF RANGE, PRICE AND SPEED?

create view view4
AS
SELECT car_name, price1, max_range, top_speed, car_brand
FROM t4_newtable
WHERE 
	car_name NOT LIKE '%Tesla%' AND (max_range BETWEEN '260' AND '270')
	AND (price1  < '59990');



*/ ADD COLUMN TO EXISTING TABLE

alter table t4_newtable
add car_brand varchar(50);

UPDATE t4_newtable
SET car_brand = CASE
	WHEN car_name lIKE '%Rolls-Royce%' THEN 'Rolls-Royce'
	WHEN car_name lIKE '%BMW%' THEN 'BMW'
	WHEN car_name lIKE '%Mercedes%' THEN 'Mercedes'
	WHEN car_name lIKE '%Porsche%' THEN 'Porsche'
	WHEN car_name lIKE '%Tesla%' THEN 'Tesla'
	WHEN car_name lIKE '%Lotus%' THEN 'Lotus'
	WHEN car_name lIKE '%Audi%' THEN 'Audi'
	WHEN car_name lIKE '%Volvo%' THEN 'Volvo'
	WHEN car_name lIKE '%Polestar%' THEN 'Polestar'
	WHEN car_name lIKE '%Ford%' THEN 'Ford'
	WHEN car_name lIKE '%Jaguar%' THEN 'Jaguar'
	WHEN car_name lIKE '%Genesis%' THEN 'Genesis'
	WHEN car_name lIKE '%Kia%' THEN 'Kia'
	WHEN car_name lIKE '%Fisker%' THEN 'Fisker Ocean'
	WHEN car_name lIKE '%Volkswagen%' THEN 'Volkswagen'
	WHEN car_name lIKE '%Skoda%' THEN 'Skoda'
	WHEN car_name lIKE '%Peugeot%' THEN 'Peugeot'
	WHEN car_name lIKE '%Mini%' THEN 'Mini Cooper'
	WHEN car_name lIKE '%Toyota%' THEN 'Toyota'
	WHEN car_name lIKE '%Nissan%' THEN 'Nissan'
	WHEN car_name lIKE '%Vauxhall%' THEN 'Vauxhall'
	WHEN car_name lIKE '%Hyundai%' THEN 'Hyundai'
	WHEN car_name lIKE '%Subaru%' THEN 'Subaru'
	WHEN car_name lIKE '%Citroen%' THEN 'Citroen'
	WHEN car_name lIKE '%Cupra%' THEN 'Cupra'
	WHEN car_name lIKE '%DS 3%' THEN 'DS 3'
	WHEN car_name lIKE '%Renault%' THEN 'Renault'
	WHEN car_name lIKE '%Honda%' THEN 'Honda'
	WHEN car_name lIKE '%Jeep%' THEN 'Jeep'
	WHEN car_name lIKE '%BYD%' THEN 'BYD'
	WHEN car_name lIKE '%Abarth%' THEN 'Abarth'
	WHEN car_name lIKE '%smart%' THEN 'Smart'
	WHEN car_name lIKE '%Fiat%' THEN 'Fiat'
	WHEN car_name lIKE '%MG%' THEN 'MG'
	WHEN car_name lIKE '%ORA%' THEN 'ORA'
	WHEN car_name lIKE '%Mazda%' THEN 'Mazda'
	WHEN car_name lIKE '%lexus%' THEN 'Lexus'
	WHEN car_name lIKE '%Maserati%' THEN 'Maserati'
	END;


	

*/ HOW MANY EVs EVERY MANUFACTURER HAVE?

SELECT count(car_name) as num_models, car_brand
FROM t4_newtable
group by car_brand;