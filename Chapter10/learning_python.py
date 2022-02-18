filename = "learning_python.txt"

# Exercise 10-1

print("----- Output from read() -----")
with open(filename) as file:
    myFile = file.read()
print(myFile)

print("----- Output from for loop inside with open -----")
with open(filename) as file:
    for line in file:
        print(line)

print("----- Output from readlines() -----")
with open(filename) as file:
    myFile=file.readlines()
print("Original list=",myFile)
for line in myFile:
    print(line)

# Exercise 10-2

print("----- Replacing Python with Javascript -----")
with open(filename) as file:
    for line in file:
        print(line.replace("Python","Javascript"))