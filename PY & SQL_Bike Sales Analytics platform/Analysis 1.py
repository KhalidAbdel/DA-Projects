
import pypyodbc
import pandas as pd
import matplotlib.pyplot as pyplot
import numpy as numpy

# Create connection with MS SQL server
server = 'LAPTOP-I57KE80H'
database = 'AdventureWorks2022'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
connection = pypyodbc.connect(connection_string)
cursor = connection.cursor()

# importing the query
cursor.execute("""SELECT
  SUM(revenue) AS total_revenue,
  Country
FROM (
  SELECT
    SUM(SalesYTD) AS revenue,
    CASE
      WHEN Name = 'Southwest' THEN 'United States of America'
      WHEN Name = 'Northeast' THEN 'United States of America'
      WHEN Name = 'Central' THEN 'United States of America'
	  WHEN Name = 'Northwest' THEN 'United States of America'
      WHEN Name = 'Southwest' THEN 'United States of America'
      WHEN Name = 'Southeast' THEN 'United States of America'
      WHEN Name = 'Canada' THEN 'Canada'
      WHEN Name = 'France' THEN 'France'
      WHEN Name = 'Germany' THEN 'Germany'
      WHEN Name = 'Australia' THEN 'Australia'
      WHEN Name = 'United Kingdom' THEN 'United Kingdom'
    END AS Country
  FROM [AdventureWorks2022].[Sales].[SalesTerritory] as t1
  INNER JOIN [AdventureWorks2022].[Sales].[SalesOrderHeader] as t2
      ON t1.TerritoryID = t2.TerritoryID
  GROUP BY Name
) AS subquery
GROUP BY Country
ORDER BY total_revenue DESC;""")


rows = cursor.fetchall()
for row in rows:
    print(row)

question3_table = pd.DataFrame(rows)
print(question3_table.head())

# Define column names
column_names = ['Country', 'total_revenue']
# Assign column names to the DataFrame
question3_table.columns = column_names

pyplot.bar(question3_table['total_revenue'],question3_table['Country'])
pyplot.legend()
pyplot.show()