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