

Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Passengers_millions = [3.789,3.530,3.570,3.131,3.221,3.602,4.082,4.325,4.091,4.244,3.891,3.607]



import matplotlib.pyplot as pyplot  

# Identyfying summer months
summer_m = [Months[5], Months[6], Months[7]]
print(summer_m)
# matching month index to the passenger numbers
summerPass_number = [Passengers_millions[5], Passengers_millions[6], Passengers_millions[7]]
print(summerPass_number)
# calculate average
avg_pass_number_summer = sum(summerPass_number) / 3
print(avg_pass_number_summer)

# winter
winter_m = [Months[9], Months[10], Months[11]]
print(winter_m)
winterPass_number = [Passengers_millions[9], Passengers_millions[10], Passengers_millions[11]]
print(winterPass_number)
avg_pass_number_winter = sum(winterPass_number) / 3
print(avg_pass_number_winter)

seasons = ['winter', 'summer']
values = [avg_pass_number_summer, avg_pass_number_winter]
pyplot.bar(seasons, values)


pyplot.show()



