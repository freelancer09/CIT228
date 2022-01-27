print("---------- Hands on 1 ----------")
foods=["pizza","pasta","taco","burrito","french toast","sushi"]
print("Favorite foods: ",foods)
numbers=[1,2,3,4,5,6]
print("Favorite numbers: ",numbers)
movies=["The Matrix", "Interstellar", "The Lord of the Rings"]
print("Favorite movies: ",movies)
combo=["pizza","pasta",1,2,"The Matrix","Interstellar"]
print("Combo list: ",combo)
print("Last food item: ",foods[-1])
print("2nd, 4th and 6th numbers: ",numbers[1],numbers[3],numbers[5])
print("Favorite movies: ",movies[0],movies[1],movies[2])
print("First food, number and movie: ",combo[0],combo[2],combo[4])

print("---------- Hands on 2 ----------")
movies.append("Avengers Endgame")
print("Added movie: ",movies)
numbers.insert(3,7)
print("Added number: ",numbers)
foods.insert(5,"ice cream")
print("Added food: ",foods)
del foods[4]
print("Deleted food: ",foods)
numbers.pop()
print("Deleted number: ",numbers)
numbers.pop(2)
print("Deleted nunber: ",numbers)

print("---------- Hands on 3 ----------")
movies.sort()
print("Sorted list: ",movies)
foods.sort()
print("Sorted list: ",foods)
print("Temp sorted list: ",sorted(numbers))
print("Unsorted list: ",numbers)
movies.reverse()
print("Reversed list: ",movies)

print("---------- Chapter 4, Hands on 1 ----------")
print("Food List:")
for food in foods:
    print(food)
print("----------")
print("Number List:")
for number in numbers:
    print(number)
print("----------")
print("Movie List:")
for movie in movies:
    print(movie)
print("----------")
print("Combo List:")
for item in combo:
    print(item)
print("----------")