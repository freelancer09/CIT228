# Exercise 9-13

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

die1 = Die()
die2 = Die(10)
die3 = Die(20)

print("6-sided die:")
i = 0
while i < 10:
    die1.roll_die()
    i += 1

print("10-sided die:")
i = 0
while i < 10:
    die2.roll_die()
    i += 1

print("20-sided die:")
i = 0
while i < 10:
    die3.roll_die()
    i += 1