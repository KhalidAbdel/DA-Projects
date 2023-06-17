
import pypyodbc
import pandas as pd
import matplotlib.pyplot as plt


# Create connection with MS SQL server
server = 'LAPTOP-I57KE80H'
database = 'AdventureWorks2022'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
connection = pypyodbc.connect(connection_string)
cursor = connection.cursor()

# importing the query
cursor.execute("""
SELECT
SquareFeetCategory,
SUM(AnnualRevenue) AS TotalRevenue,
SUM(TotalEmployees) AS TotalEmployees
FROM (
SELECT
Name,
AnnualRevenue,
SUM(NumberEmployees) AS TotalEmployees,
CASE
WHEN SUM(SquareFeet) >= 1000 AND SUM(SquareFeet) <= 10000 THEN '1k-10k'
WHEN SUM(SquareFeet) >= 10000 AND SUM(SquareFeet) <= 20000 THEN '20k-30k'
WHEN SUM(SquareFeet) >= 20000 AND SUM(SquareFeet) <= 30000 THEN '20k-30k'
WHEN SUM(SquareFeet) >= 30000 AND SUM(SquareFeet) <= 40000 THEN '30k-40k'
WHEN SUM(SquareFeet) >= 40000 AND SUM(SquareFeet) <= 50000 THEN '40k-50k'
WHEN SUM(SquareFeet) >= 50000 AND SUM(SquareFeet) <= 60000 THEN '50k-60k'
WHEN SUM(SquareFeet) >= 60000 AND SUM(SquareFeet) <= 70000 THEN '60k-70k'
WHEN SUM(SquareFeet) >= 70000 AND SUM(SquareFeet) <= 80000 THEN '70k-80k'
ELSE 'Other'
END AS SquareFeetCategory
FROM [AdventureWorks2022].[Sales].[vStoreWithDemographics]
GROUP BY Name, AnnualRevenue
) AS subquery
GROUP BY SquareFeetCategory
ORDER BY SquareFeetCategory DESC
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

emp_revenue_storeSize = pd.DataFrame(rows)
print(emp_revenue_storeSize.head())


# Create a DataFrame from the SQL query results
emp_revenue_storeSize = pd.DataFrame(rows, columns=['StoreSize', 'TotalRevenue', 'TotalEmployees'])


import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Create a scatter plot
plt.scatter(emp_revenue_storeSize['StoreSize'], emp_revenue_storeSize['TotalRevenue'], s=emp_revenue_storeSize['TotalEmployees'], alpha=0.7)

# Set labels and title
plt.xlabel('Store Size in Sqrft')
plt.ylabel('Total Revenue (in Millions)')
plt.title('Relationship between Store Size and Revenue')
plt.grid()

# Add annotations for total number of employees
for i in range(len(emp_revenue_storeSize)):
    x = emp_revenue_storeSize['StoreSize'][i]
    y = emp_revenue_storeSize['TotalRevenue'][i]
    employees = emp_revenue_storeSize['TotalEmployees'][i]
    plt.annotate(f'{employees} employees', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Format y-axis tick labels in millions
formatter = mticker.FuncFormatter(lambda x, pos: f'{x/1e6:.0f}M')
plt.gca().yaxis.set_major_formatter(formatter)

# Reverse the x-axis
plt.gca().invert_xaxis()

# Show the plot
plt.show()

########################################################


