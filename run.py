"""Import randint from random module"""
from random import randint


class Board:
    """Game board for Battleship class. Sets board size, the player's name,
    and displays the boards for both the player and computer.
    """
    def __init__(self, size=8):
        self.size = size
        self.grid = [[' '] * size for _ in range(size)]
        self.row_labels = [str(i+1) for i in range(size)]
        self.col_labels = 'ABCDEFGH'

    def display(self):
        print('  ' + ' '.join(self.col_labels))
        for idx, row in enumerate(self.grid):
            print(self.row_labels[idx] + '|'.join(row) + '|')

    def place_ship(self):
        for _ in range(4):
            while True:
                row = randint(0, self.size - 1)
                col = randint(0, self.size - 1)
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = '@'
                    break


def new_game():
    """New game function.
    Starts a new game of Battleship.
    """
    print("Welcome to my Battleship game!")
    player_name = input("What is your name? ")
    print("\n")
    print(f"Hello, {player_name}! Let's play Battleship.")

    player_board = Board()
    computer_board = Board()

    player_board.place_ship()
    computer_board.place_ship()

    print(f"\n{player_name}'s Board:")
    player_board.display()
    print("\nComputer's Board:")
    computer_board.display()


# Call the new_game function to start the game
new_game()
