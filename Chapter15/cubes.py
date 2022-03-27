import matplotlib.pyplot as plt

# Plot 1
cubed=[]
inputVal = [1, 2, 3, 4, 5]
for num in inputVal:
    cubed.append(num*num*num)
ax1 = plt.subplot(1,2,1)
ax1.plot(inputVal, cubed, marker='o', ls='dashdot', c='green', lw='2.0')
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

# Plot 2
pow=[]
for num in inputVal:
    pow.append(num**2)
ax2 = plt.subplot(1,2,2)
plt.style.use("seaborn-poster")
ax2.plot(inputVal, pow, color='goldenrod', lw='2', marker='^')
plt.title("Numbers Raised", color='goldenrod')
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid()

plt.suptitle("Fun with Numbers", c='green', fontfamily='Comic Sans MS', fontsize='20')
plt.subplots_adjust(top=0.8, wspace=1)
plt.show()