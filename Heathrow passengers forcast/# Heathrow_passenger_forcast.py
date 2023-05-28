
# 230521_Task1:
# Produce a chart to compare the average number of passengers in the winter to the summer:
# Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# Passengers_millions = [3.789,3.530,3.570,3.131,3.221,3.602,4.082,4.325,4.091,4.244,3.891,3.607]


# import matplotlib.pyplot as pyplot  
# # Identyfying summer months
# summer_m = [Months[5], Months[6], Months[7]]
# print(summer_m)
# # matching month index to passenger numbers
# summerPass_number = [Passengers_millions[5], Passengers_millions[6], Passengers_millions[7]]
# print(summerPass_number)
# # calculate average
# avg_pass_number_summer = sum(summerPass_number) / 3
# print(avg_pass_number_summer)

# # winter
# winter_m = [Months[9], Months[10], Months[11]]
# print(winter_m)
# winterPass_number = [Passengers_millions[9], Passengers_millions[10], Passengers_millions[11]]
# print(winterPass_number)
# avg_pass_number_winter = sum(winterPass_number) / 3
# print(avg_pass_number_winter)

# #create variables 'season' and 'values'
# seasons = ['winter', 'summer']
# values = [avg_pass_number_summer, avg_pass_number_winter]

# #customise plot
# pyplot.barh(seasons, values)
# pyplot.show()





# 230524_Task2:
# Heathrow is expecting a 9% forecast in passenger numbers next year. 
# Work out how many passengers are expected in total during next summer.
# produce a line chart comparing historic passenger numbers to next year’s forecasts

# Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# Passengers_millions = [3.789,3.530,3.570,3.131,3.221,3.602,4.082,4.325,4.091,4.244,3.891,3.607]

# import numpy as numpy
# import matplotlib.pyplot as pyplot
# #finding next year overall increase
# NxtYear_forcast = numpy.array(Passengers_millions) * 1.09
# print (NxtYear_forcast)
# #finding the forcasted increase only for summer
# NxtSummer_forcast = numpy.mean(NxtYear_forcast[5:8])
# print(NxtSummer_forcast)
# pyplot.plot(Months, Passengers_millions, label = 'Current year')
# pyplot.plot(Months, NxtYear_forcast, label = 'next year')
# pyplot.legend()
# pyplot.show()





#260523_Task 3:
#import data from xls and Compare passenger numbers now to the pre-covid levels

import numpy as numpy
import pandas as pandas
import matplotlib.pyplot as pyplot
df = pandas.read_excel(r'C:\Users\khali\Desktop\DA-LON4\T Heathrow Passengers\250523_heathrowflightpassengerdataset120123.xlsx')


print(df.info())
print(df.shape)
print(df[['Date', 'Heathrow_Passengers']])
#FINDING QUICK SUMMARY ABOUT THE DATA
print(df.describe())
#finding MEAN passenger numbers for 2019-2022 inclusive (pre and post covid)
pre_covid = df.Heathrow_Passengers[:13]
mean_preC = round(numpy.mean(pre_covid),0)
print(mean_preC)
post_covid = df.Heathrow_Passengers[13:]
mean_postC = numpy.mean(post_covid[13:])
print(mean_postC )

 #calculating total passengers
total_passengers = numpy.sum(df.Heathrow_Passengers)
print(total_passengers)
#calculating % of passenger numbers (pre covid) 
totalpsg_precovid_pc = numpy.sum(df.Heathrow_Passengers[:13]) / numpy.sum(df.Heathrow_Passengers) * 100
print(totalpsg_precovid_pc)

# summary = pandas.pivot_table(df)
# print(summary)

#defining variables 
# xaxis = df['Date']
# yaxis = df['Heathrow_Passengers']
# pyplot.plot(xaxis, yaxis)
# pyplot.show()

