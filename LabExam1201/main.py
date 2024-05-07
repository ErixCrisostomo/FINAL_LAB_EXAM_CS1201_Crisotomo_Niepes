from Utils.dice_game.py import
from Utils.user_manager.py import

def menu(self):
    print("Welcome to Dice Game!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = str(input(print("Enter your Choice or Leave Blank to Cancel.")))

    if choice == "1":
        user_manager.register(self)
    elif choice == "2":
        user_manager.login(self)
    elif choice == "3":
        return
    