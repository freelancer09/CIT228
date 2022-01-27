import random
number = random.randrange(10,100)
numbers = list(range(number))
print(numbers)
print("Max:",max(numbers))
print("Min:",min(numbers))
print("Sum:",sum(numbers))
print("Average:",sum(numbers)/len(numbers))