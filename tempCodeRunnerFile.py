import pandas as pandas
import numpy as numpy
import matplotlib.pyplot as pyplot

ev_data = pandas.read_csv(r'C:\Users\khali\Desktop\DA-LON4\T EV-data for python\IEA-EV-dataEV charging pointsEVHistorical.csv')
ev_sales = pandas.read_csv(r'C:\Users\khali\Desktop\DA-LON4\T EV-data for python\IEA-EV-dataEV salesCarsHistorical.csv')
# print(ev_sales.info())
# print(ev_data.head())
# print(ev_sales.describe())


# TOTAL NUMBER OF EV SOLD BY REGION PER YEAR
EV_count = ev_sales.groupby(['region','year'])['value'].sum()
print(EV_count.head)

# EV_count = EV_count.reset_index()
# graph_data = EV_count.groupby('region')
# for region, region_data in graph_data:
#     pyplot.plot(region_data['year'], region_data['value'], label=region)

# pyplot.xlabel('Year')
# pyplot.ylabel('Total EV Sales')
# pyplot.title('Electric Vehicle Sales by Region and Year')
# pyplot.legend()
# pyplot.grid(True)
# pyplot.show()



# NUMBER OF CHARGING POINTS PER REGION (INCLUSIVE)
chargingpoints_count = ev_data.groupby(['region', 'year'])['value'].sum()
print(chargingpoints_count)

# REMOVING COLUMNS FROM EV_data
removed_columns = ev_data.drop(['category', 'parameter', 'mode', 'unit'], axis =1)
filtered_row = ev_sales[ev_sales['powertrain'] == 'BEV']

# DISTRIBUTION BY TYPE OF POWERTRAIN (BEV / PHEV) INCLUSIVE
total_powertrain = ev_sales['powertrain'].count()
print(total_powertrain)
powertrain_type = ev_sales.groupby(['powertrain'])['year'].count()
print(powertrain_type)

pyplot.pie(powertrain_type, autopct='%1.1f%%')
pyplot.legend()
pyplot.show()

# CALCULATING POWERTRAIN DISTRIBUTION PERCENTAGE
percentage = round(powertrain_type / total_powertrain * 100, 2)
print(percentage)







