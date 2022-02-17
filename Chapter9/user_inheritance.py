class User:
    def __init__(self,first_name,last_name,user_name,password,email,login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.email = email
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has a username of {self.user_name}, a password of {self.password} and an email address of {self.email}")
    def greet_user(self):
        print(f"Welcome back {self.first_name}")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name} has tried to login {self.login_attempts} times!")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The number of attempts has been reset to: {self.login_attempts}")

class Admin(User):
    def __init__(self,first_name,last_name,user_name,password,email,login_attempts, privileges):
        super().__init__(first_name,last_name,user_name,password,email,login_attempts)
        self.privileges = Privileges(privileges)

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

# Exercise 9-8
print("---------- Exercise 9-8 ----------")
user1 = Admin("George","Jetson","georgejetson","astro123","george@jetson.net",0,["can add post","can delete post","can ban user"])
user1.greet_user()
user1.describe_user()
print(f"{user1.user_name} has the following privileges:")
user1.privileges.show_privileges()