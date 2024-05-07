import random

class DiceGame:
    def load_scores():
        pass

    def save_scores():
        pass

    def menu():
        print("Welcome to Dice Game!")
        print("1. Play")
        print("2. Show Top Scores")
        print("3. Log Out")

        choice = str(input("Enter your Choice or Leave Blank to Cancel: "))

        if choice == "1":
            play_game()
        elif choice == "2":
            show_topscores()
        elif choice == "3":
            logout()

    def logout():
        pass
    def show_topscores():
        pass
    
    def play_game():
        dice_rolls = random.randint(1,6)

        print("You have rolled: ")
        print(dice_rolls)
        print("CPU have rolled: ")
        print(dice_rolls)
        print("You have rolled: ")
        print(dice_rolls)
        print("CPU have rolled: ")
        print(dice_rolls)
        print("You have rolled: ")
        print(dice_rolls)
        print("CPU have rolled: ")
        