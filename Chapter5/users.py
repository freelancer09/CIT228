print("---------- Exercise 5-10 ----------")
current_users = ["admin","mike","aaron","nathan","abe"]
new_users = ["don","Abe","aaron","russel","steve"]
lower_users = []
for user in current_users:
    lower_users.append(user.lower())
for user in new_users:
    if user.lower() in lower_users:
        print(user,"has been taken, please use something else.")
    else:
        print(user,"is available.")