# WSF2 - Fastest 2-minute wind speed
# WDF2 - Direction of fastest 2-minute wind
# AWND - Average wind speed
# WSF5 - Fastest 5-second wind speed
# WDF5 - Direction of fastest 5-second wind
# WT01 - Fog, ice fog, or freezing fog (may include heavy fog)
# TMAX - Maximum temperature
# WT03 - Thunder
# TAVG - Average Temperature.
# TMIN - Minimum temperature
# PRCP - Precipitation
# WT08 - Smoke or haze
# Data from: https://www.ncdc.noaa.gov/cdo-web/

import csv
import matplotlib.pyplot as plt

dates=[]
tmax=[]
tmin=[]
prcp=[]
awnd=[]
wsf2=[]
wt03=[]
with open('noaa-hawaii.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row = next(csv_reader)
    for row in csv_reader:
        dates.append(row[2])
        awnd.append(float(row[3]))
        prcp.append(float(row[4]))
        tmax.append(float(row[6]))
        tmin.append(float(row[7]))
        wsf2.append(float(row[10]))
        if (row[13]): 
            wt03.append(int(row[13]))
        else:
            wt03.append(0)

plt.scatter(dates, tmax, c=tmax, cmap=plt.cm.Reds, label="TMAX")
plt.scatter(dates, tmin, c=tmin, cmap=plt.cm.Blues, label="TMIN")
plt.ylabel("Temperature (F)")
plt.xlabel("Day")
plt.legend(loc="best")
plt.suptitle("Honolulu Temps (2021)")
plt.tick_params(bottom=False, labelbottom=False)
plt.show()

plt.hist(prcp, bins=8)
plt.suptitle("Honolulu Precipitation (2021)")
plt.ylabel("Number of Days")
plt.xlabel("Inches")
plt.show()

plt.hist(wt03, bins=2)
plt.suptitle("Honolulu Thunder (2021)")
plt.ylabel("Number of Days")
plt.xlabel("No / Yes")
plt.tick_params(bottom=False, labelbottom=False)
plt.show()

plt.plot(dates, awnd)
plt.suptitle("Honolulu Average Wind Speed (2021)")
plt.tick_params(bottom=False, labelbottom=False)
plt.ylabel("Miles per Hour")
plt.xlabel("Day")
plt.show()

plt.plot(dates, wsf2)
plt.suptitle("Honolulu Fastest 2 minute Wind Speed (2021)")
plt.tick_params(bottom=False, labelbottom=False)
plt.ylabel("Miles per Hour")
plt.xlabel("Day")
plt.show()

labels = 'Hawaii', 'Alaska', 'Flordia', 'Washington DC', 'Other'
num = [83, 5, 15, 10, 3]
plt.pie(num, labels=labels, autopct='%3.1f%%')
plt.axis('equal')
plt.suptitle("Villian survey: Dream location")
plt.show()