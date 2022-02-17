from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,user_name,password,email,login_attempts, privileges):
        super().__init__(first_name,last_name,user_name,password,email,login_attempts)
        self.privileges = Privileges(privileges)