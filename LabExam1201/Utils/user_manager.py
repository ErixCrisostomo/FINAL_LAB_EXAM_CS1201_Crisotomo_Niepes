from Utils.user import User
from Utils.dice_game import DiceGame

user_database = {}

class UserManager:
    

    def load_users():
        pass

    def save_users():
        pass

    def validate_username():
        pass

    def validate_password():
        pass

    def register(self):
        print("Please Input your Desired Username and Password")
        username = str(input("Enter Username(At least 4 characters) or Leave Blank to Cancel: "))
        if len(username) < 4:
            print("Username too short.")
            return
        elif len(username) > 4:
            print("Username is too long.")
            return
        elif len(username) == 4:
            print("Username Saved.")  
            user_database[username] = {
                "username": username
            }
        password = str(input("Enter Password(At least 8 characters) or Leave Blank to Cancel: "))
        if len(password) < 4:
            print("Password too short.")
            return
        elif len(password) > 4:
            print("Password is too long.")
            return
        elif len(password) == 4:
            print("Password Saved.")  
            user_database[username] = {
                "password": password
            }

    def login(username):
        print("Please Enter your Username and Password.")
        username = str(input("Username: "))
        password = str(input("Password: "))
        if username in user_database and user_database [username]["password"] == password:
            print("You have succesfully logged in.")
            DiceGame.menu()
                



