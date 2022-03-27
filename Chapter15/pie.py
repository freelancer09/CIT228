import matplotlib.pyplot as plt

labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
num = [376, 348, 153, 104, 19]
explode = (.1, 0, 0, 0, 0)
wedgeColors=('lightgreen', 'magenta', 'teal', 'white', 'tan') 

fig1, ax1 = plt.subplots()
ax1.pie(num, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=315, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle("Popular Graphic Formats on the Web")

plt.show()