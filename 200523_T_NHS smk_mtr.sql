



/* MATERNETIES PER REGION

SELECT 
	DISTINCT(OrgName) AS Region, Measure, SUM(Value) AS NumberMaternities
FROM 
	[DA-LON4].[dbo].[t_nhs2]
WHERE 
	Measure = 'Number of maternities' AND OrgName NOT LIKE '%NHS%' 
	AND OrgName NOT LIKE '%London%' AND OrgName != 'England'
GROUP BY 
	OrgName, Measure
ORDER BY
	NumberMaternities DESC;



/* TOTAL MATERNETIES IN ENGLAND INCLUSIVE

SELECT 
	DISTINCT(OrgName), Measure, SUM(Value) AS NumberMaternities
FROM 
	[DA-LON4].[dbo].[t_nhs2]
WHERE 
	Measure = 'Number of maternities' AND OrgName = 'England' 
GROUP BY 
	OrgName, Measure
ORDER BY
	NumberMaternities DESC;




/* COMPARISON OF MEASURES

SELECT 
	Measure, SUM(Value) AS NumberMaternities
FROM 
	[DA-LON4].[dbo].[t_nhs2]
WHERE 
	Measure = 'Women known to be non-smokers at time of delivery' OR
	Measure = 'Women known to be smokers at time of delivery' OR
	Measure = 'Women whose smoking status was not known at time of delivery'
	AND OrgName = 'England' 
GROUP BY 
	Measure
ORDER BY
	NumberMaternities DESC;



/* WHICH NHS AREA HAS THE HIGHEST SMOKING MATERNITY RATE?

SELECT 
	OrgName, Measure, max(Value) AS NumberMaternities
FROM 
	[DA-LON4].[dbo].[t_nhs2]
WHERE
	Measure = 'Women known to be smokers at time of delivery' AND OrgName LIKE '%NHS%'
GROUP BY 
	OrgName,  Measure
ORDER BY
	NumberMaternities DESC;


/* NHS NORTH EAST AND NORTH CUMBRIA HAS THE HIGHEST RATE OF WOMEN WHO IDENTIFY AS SMOKERS DURING MATERNITY
		
/* NOW I SUBTRACT THE TOTAL NUMBER OF SMOKERS FROM THE TOTAL MATERNITY NUMBERS FOR ALL AREAS AND ADD PERCENTAGE

		select 
		tb1.OrgName, 
		tb1.Measure, 
		totalMat_num - NumberofSmokersMaternities AS difference
		FROM (
		SELECT
            OrgName,
            Measure,
            SUM(Value) AS totalMat_num
        FROM
            [DA-LON4].[dbo].[t_nhs2]  
        WHERE
            Measure = 'Number of maternities'
        GROUP BY
            OrgName,
            Measure) AS tb1
			JOIN (SELECT
            OrgName,
            Measure,
            SUM(Value) AS NumberofSmokersMaternities
        FROM
            [DA-LON4].[dbo].[t_nhs2]
        WHERE
            Measure = 'Women known to be smokers at time of delivery'
        GROUP BY
            OrgName,
            Measure) AS tb2 
		ON tb1.OrgName = tb2.OrgName
ORDER BY
    difference DESC;