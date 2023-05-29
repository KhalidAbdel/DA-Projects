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
print(EV_count)

# TOP 5 COUNTRIES WITH HIGHEST NUMBER OF EV SALES IN 2022
top_regions = ev_sales[ev_sales.region.isin(['World', 'China', 'EU27', 'USA',]) & ev_sales.year.isin([2022])].head()
print(top_regions)


EV_count = EV_count.reset_index()
graph_data = EV_count.groupby('region')
for region, region_data in graph_data:
    pyplot.plot(region_data['year'], region_data['value'], label=region)

pyplot.xlabel('Year')
pyplot.ylabel('Total EV Sales')
pyplot.title('Electric Vehicle Sales by Region and Year')
pyplot.legend()
pyplot.grid(True)
pyplot.show()



# REMOVING COLUMNS FROM EV_data
removed_columns = ev_data.drop(['category', 'parameter', 'mode', 'unit'], axis =1)
filtered_row = ev_sales[ev_sales['powertrain'] == 'BEV']

# DISTRIBUTION BY TYPE OF POWERTRAIN (BEV / PHEV) INCLUSIVE
total_powertrain = ev_sales['powertrain'].count()
print(total_powertrain)
powertrain_type = ev_sales.groupby(['powertrain'])['year'].count()
print(powertrain_type)

pyplot.pie(powertrain_type, labels=powertrain_type.index, autopct='%1.1f%%')
pyplot.legend()
pyplot.title('plug-in hybrid electric vehicle (PHEV) vs battery-powered electric vehicle (BEV)')
pyplot.show()
#summerize by finding which countries has most BEV and which produce most CO2

# CALCULATING POWERTRAIN DISTRIBUTION PERCENTAGE
percentage = round(powertrain_type / total_powertrain * 100, 2)
print(percentage)

# NUMBER OF CHARGING POINTS PER REGION (INCLUSIVE)
chargingpoints_count = ev_data.groupby(['region', 'year'])['value'].sum()
print(chargingpoints_count)

unique = chargingpoints_count.unique()
period = ev_sales['year']
pyplot.plot(range(len(unique)), unique)
pyplot.legend()
pyplot.show()

# DISTRIBUTION BY CHARGER TYPE (FAST/SLOW) 
charging_type = ev_data.groupby(['charging type'])['year'].count()
print(charging_type)

colors = ['purple','grey']
pyplot.bar(charging_type, label = charging_type.index, height = 4, color = colors)
pyplot.legend()
pyplot.title('Distribution by charger speed') 
pyplot.show()





