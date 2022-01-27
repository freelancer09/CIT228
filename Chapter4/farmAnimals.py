animals=["horse","cow","pig","chicken","rooster","goat"]
animals2=animals[:]
animals2.append("cat")
animals2.append("dog")
animals2.append("llama")
animals2.append("mink")
print("---------- Original List ----------")
for animal in animals:
    print(animal)
print("---------- New List ----------")
for animal in animals2:
    print(animal)

print("The first three items in the list are",animals2[0:3])
print("Three items from the middle of the list are:",animals2[2:5])
print("The last three items in the list are:",animals2[7:10])