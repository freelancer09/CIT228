rivers = {
    "Nile" : "Egypt",
    "Mississippi" : "United States",
    "Amazon" : "Brazil",
}
print("----- Rivers and Countries -----")
for key, value in rivers.items():
    print("The",key,"runs through",value)
print("----- Rivers  -----")
for value in rivers:
    print(value)
print("----- Countries  -----")
for value in rivers.values():
    print(value)