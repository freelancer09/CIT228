glossary = {
    "Dictionary" : "Python data type that stores key:value pairs",
    "Syntax" : "Rules you need to follow within a programing language",
    "Variable" : "Reserved memory locations to store values",
    "Constant" : "Value assigned to variables that do not change.",
    "List" : "Python data type that stores multiple items under a single variable name",
    "Key" : "Value used to access data stored in the dictionary",
    "Del" : "Command used to remove a key:value pair from the dictionary",
    "Append" : "Command used to add to the end of a list",
    "Insert" : "Command used to add an item anywhere in a list",
    "Pop" : "Command used to remove the last item from a list and save the value removed",
}
print("----- Python Glossary -----")
#print("Constant:")
#print("\t",glossary["Constant"])
#print("Dictionary:")
#print("\t",glossary["Dictionary"])
#print("List:")
#print("\t",glossary["List"])
#print("Syntax:")
#print("\t",glossary["Syntax"])
#print("Variable:")
#print("\t",glossary["Variable"])
for key, value in glossary.items():
    print(key)
    print("\t",value)