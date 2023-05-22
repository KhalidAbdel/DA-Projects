
import matplotlib.pyplot as pyplot

Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Passengers_millions = [3.789, 3.530, 3.570, 3.131, 3.221, 3.602, 4.082, 4.325, 4.091, 4.244, 3.891, 3.607]

max_pgr = max(Passengers_millions)
print(max_pgr)

index1 = Passengers_millions.index(max_pgr)
busiest_month = Months[index1]
print(busiest_month)

pyplot.plot(Months,Passengers_millions)
pyplot.show()
