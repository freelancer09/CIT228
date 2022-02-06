sandwich_orders = ["Ham","Pastrami","Italian","Pepperoni","Pastrami","PB&J","Pastrami"]
finished_sandwiches = []
print("I'm sorry, we are out of pastrami!!!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

print("Sandwiches that were made today include:")
for sandwich in finished_sandwiches:
    print(sandwich.title())