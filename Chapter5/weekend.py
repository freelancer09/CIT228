import datetime
# weekdays tuple
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# retrieving current date
now = datetime.date.today()
# retrieve the day of the week which is an integer
dayOfWeek = now.weekday()
# subscript into weekDays using the dayOfWeek
today = weekDays[dayOfWeek]
# calculate and print days until the weekend
daysToWeekend = 6 - dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend")
# flag to only print 1 quote in for loop
quotePrinted = "false"
# prints week days left until weekend with a quote
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == "false":
        print(left, " Sunday is my funday!")
        quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, " Sigh.... Back to the daily grind")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, " Almost there...")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, " Woo hoo, the weekend")
        quotePrinted = "true"
    else:
        print (left)