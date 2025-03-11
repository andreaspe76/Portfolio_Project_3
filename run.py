# Import randit from random module
from random import randint


def new_game():
    print("Welcome to my Battleship game!")
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}! Let's play Battleship.")


new_game()