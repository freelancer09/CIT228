number = input("Please enter a number and I will tell you if it is a multiple of 10: ")
number = int(number)
if (number % 10) == 0:
    print("The number",number,"is a multiple of ten.")
else:
    print("The number",number,"is not a multiple of ten.")