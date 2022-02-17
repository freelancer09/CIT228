from user import User
from admin import Admin
from privileges import Privileges

# Exercise 9-8
print("---------- Exercise 9-8 ----------")
user1 = Admin("George","Jetson","georgejetson","astro123","george@jetson.net",0,["can add post","can delete post","can ban user"])
user1.greet_user()
user1.describe_user()
print(f"{user1.user_name} has the following privileges:")
user1.privileges.show_privileges()