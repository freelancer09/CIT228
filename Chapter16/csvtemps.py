import csv
import matplotlib.pyplot as plt

dates=[]
tmax=[]
tmin=[]
with open('temps.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row = next(csv_reader)
    for row in csv_reader:
        dates.append(row[2])
        tmax.append(float(row[4]))
        tmin.append(float(row[5]))

plt.scatter(dates, tmax, c=tmax, cmap=plt.cm.Reds, label="TMAX")
plt.scatter(dates, tmin, c=tmin, cmap=plt.cm.Blues, label="TMIN")

plt.ylabel("Temperature (F)")
plt.xlabel("Days")
plt.legend(loc="best")
plt.suptitle("Traverse City Temps (Jan - March)")

plt.show()