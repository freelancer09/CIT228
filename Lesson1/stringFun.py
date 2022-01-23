# exercise 1 - use your own first and last name
print("------------------------------")
print("Exercise 1")
name = "michael mclaughlin"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# exercise 2 - make up your own noun, adjective, verb and ending
# use concatention to create sentence1
# use an f-string to create sentence2
print("------------------------------")
print("Exercise 2")
noun = "bird"
adj = "impatient"
verb = "flew"
ending = "the coop"
sentence1 = "the " + adj + " " + noun + " " + verb + " " + ending
sentence2 = f"the {adj} {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())

# exercise 3 - find a quote or an exerpt from a poem or book that you like, store it in a variable and print it out.
print("------------------------------")
print("Exercise 3")
quote = "It's a dangerous business, Frodo, going out your door. You step onto the road, and if you don't keep your feet, there's no knowing where you might be swept off to."
author = "J.R.R. Tolkien, The Lord of the Rings"
print(quote)
print(author)

#exercise 4 - create a two column printout using \t and \n
print("------------------------------")
print("Exercise 4")
color = "Blue"
car = "Ford"
food = "Pizza"
city = "Traverse City"
print("Color\t\t",color,"\nCar\t\t",car,"\nFood\t\t",food,"\nCity\t\t",city)