guests = input("How many people are in your dinner party?: ")
guests = int(guests)
if (guests > 8):
    print("Please wait in the lounge until a table is available.")
else:
    print("Your table is ready, please follow me.")