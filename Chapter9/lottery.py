from random import choice

# Exercise 9-14

choices = [1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E"]
winners = [choice(choices),choice(choices),choice(choices),choice(choices)]
print("Winning ticket:")
for winner in winners:
    print(winner)

# Exericse 9-15

my_ticket = [choice(choices),choice(choices),choice(choices),choice(choices)]
i = 1
while my_ticket[0] not in winners or my_ticket[1] not in winners or my_ticket[2] not in winners or my_ticket[3] not in winners:
    i += 1
    my_ticket = [choice(choices),choice(choices),choice(choices),choice(choices)]

print(f"It took {i} tickets to win!")