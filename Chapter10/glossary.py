import json

filename = "glossary.json"

def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite != "q":
        with open(filename, "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print(filename,"has been created")

def read():
    try:
        with open(filename) as read_file:
            glossaryFile = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")
    else:
        print("----- Python Glossary -----")
        for key, value in glossaryFile.items():
            print(key)
            print("\t",value)

def append(new_item):
    with open(filename, "r+") as add_file:
        glossaryFile = json.load(add_file)
        glossaryFile.update(new_item)
        add_file.seek(0)
        json.dump(glossaryFile, add_file, indent=4, sort_keys=True)
        print("Data has been added to",filename)

def menu():
    selection = int(input("1-Create file, 2-Read file, 3-Add to file, 4-Quit  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-Create file, 2-Read file, 3-Add to file, 4-Quit  "))
    return selection

def get_key():
    name=input("Enter a glossary term: ")
    term=name.split()[0]
    term=term.lower()
    return term

def get_value():
    definition=input("Enter the term definition: ")
    return definition

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

choice=menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        user=get_key()
        num=get_value()
        new_dictionary_entry={user:num}
        append(new_dictionary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()