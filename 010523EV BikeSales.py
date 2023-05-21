mountain_bike_sales = [106, 110, 198, 292, 300, 350, 302, 340, 390, 410, 440, 490]
electric_bike_sales = [130, 160, 110, 140, 250, 290, 301, 312, 315, 345, 390, 401]

mountain_bike_costs = [100, 101, 118, 212, 250, 301, 289, 301, 377, 377, 401, 403]
electric_bike_costs = [101, 106, 101, 101, 201, 201, 201, 212, 215, 275, 280, 285]


#for the last 3 months, which type of bike had the highest sales growth as a percentage?

import numpy as numpy

sales1 = mountain_bike_sales[-3:]
sales2 = electric_bike_sales[-3:]

increase1 = round((mountain_bike_sales[-1] - mountain_bike_sales[-3]) / mountain_bike_sales[-1] * 100, 2)
increase2 = round((electric_bike_sales[-1] - electric_bike_sales[-3]) / electric_bike_sales[-1] *100, 2)
print(increase1)
print(increase2)

#for the last 3 months, which type of bike had the highest profit growth as a %

profit_mtn = numpy.array(mountain_bike_sales) - (mountain_bike_costs)
qtr_profit_mtn = round((profit_mtn[-1] - profit_mtn[-3]) / profit_mtn[-1] * 100,2)
print(qtr_profit_mtn)

profit_elc = numpy.array(electric_bike_sales) - (electric_bike_costs)
qtr_profit_elc = round((profit_elc[-1] - profit_elc[-3]) / profit_elc[-1] * 100,2)
print(qtr_profit_elc)


print ('Insights: \n' + '* Mountain bike sales increased by ' + str(increase1) + '% \n' + 
      'compared to electric bike sales which has only increased by ' + str(increase2) + '%. \n'+
      '* Durint the same quarter, profits from mountain bikes also grew by ' + str(qtr_profit_mtn)+ '% \n'+
      'while electric bikes recorded profit of only ' + str(qtr_profit_elc)+ '%.')
