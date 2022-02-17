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

# Exercise 9-3
print("---------- Exercise 9-3 ----------")
user1 = User("George","Jetson","georgejetson","astro123","george@jetson.net")
user1.greet_user()
user1.describe_user()
user2 = User("Wilma","Flintstone","flinty","pebbles","wilma@flint.net")
user2.greet_user()
user2.describe_user()
user3 = User("Betty","Rubble","bets","bambam","bets@rub.com")
user3.greet_user()
user3.describe_user()

# Exercise 9-5
print("---------- Exercise 9-5 ----------")
user4 = User("Flo","Schmoe","flow","eieiflo","flo@schmoe.net",0)
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
print(f"{user4.first_name} you have exceeded the number of login attempts.")
user4.reset_login_attempts()
print("Your account has been locked for 30 minutes, please try back later or call tech support for help!")