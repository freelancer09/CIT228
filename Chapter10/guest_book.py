import os, random

filename = "guest_book.txt"

"""
guest = input("What is your name (q to quit)?:")
with open(filename,"w") as guestBook:
    while guest != "q":
        print("Greetings,",guest)
        guest += "\n"
        guestBook.write(guest)        
        guest = input("What is your name (q to quit)?:")
"""

if os.path.exists(filename):
    os.remove(filename)

rooms = []

guest = input("What is your name (q to quit)?:")
with open(filename,"w") as guestBook:
    while guest != "q" and len(rooms) < 51:
        room = random.randint(1,50)
        while room in rooms:
            room = random.randint(1,50)
        print(f"{guest} will be staying in room {room}")
        rooms.append(room)
        guest += ": Room " + str(room) + "\n"
        guestBook.write(guest)        
        guest = input("What is your name (q to quit)?:")

print(f"----- {len(rooms)} Rooms Booked -----")
with open(filename) as guestBook:
    for line in guestBook:
        print(line)