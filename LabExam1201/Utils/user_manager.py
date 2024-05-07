class UserManager:
    user_database = {}

    def load_users():

    def save_users():


    def validate_username():

    def validate_password():

    def register(self):
        print("Please Input your Desired Username and Password")
        username = str(input("Enter Username(At least 4 characters) or Leave Blank to Cancel: "))
        if len(username) < 4:
            print("Username too short.")
            return
        elif len(username) > 4:
            print("Username is too long.")
            return
        elif len(username) = 4:
            print("Username Saved.")  
            user_database = {
                "username" = username
            }
        password = str(input("Enter Password(At least 8 characters) or Leave Blank to Cancel: "))
        if len(password) < 4:
            print("Password too short.")
            return
        elif len(password) > 4:
            print("Password is too long.")
            return
        elif len(password) = 4:
            print("Password Saved.")  
            user_database = {
                "password" = password
            }

    def login(username):
        print("Please Enter your Username and Password.")
        username = str(input("Username: "))
        if username in user_database:
            password = str(input("Password: "))
            if password 


