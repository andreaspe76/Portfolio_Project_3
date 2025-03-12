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

    def display(self, show_ships=False):
        """Print the board with row and column labels.
        """
        print('  ' + ' '.join(self.col_labels))
        for idx, row in enumerate(self.grid):
            display_row = [cell if cell == '' or show_ships
                           else ' ' for cell in row]
            print(self.row_labels[idx] + '|'.join(display_row) + '|')

    def place_ship(self):
        """Place 4 ships randomly
        on the player's and computer's boards.
        """
        for _ in range(4):
            while True:
                row = randint(0, self.size - 1)
                col = randint(0, self.size - 1)
                if self.grid[row][col] == ' ':
                    self.grid[row][col] = '@'
                    break

    def valid_cl(self, col):
        """Check if the player's column choice is valid.
        """
        return col in self.col_labels

    def valid_rw(self, row):
        """Check if the player's row choice is valid.
        """
        return row in self.row_labels

    def check_move(self, col_index, row_index):
        """Check if the player's move is a hit or miss.
        """
        return self.grid[row_index][col_index] == '@'

    def mark_move(self, col_index, row_index, hit):
        """Mark the player's and computer's move on the board.
        """
        if hit:
            self.grid[row_index][col_index] = '*'
        else:
            self.grid[row_index][col_index] = 'X'


def new_game():
    """New game function.
    Starts a new game of Battleship.
    """
    print("Welcome to my Battleship game!")
    player_name = input("What is your name? ")
    print("\n")
    print(f"Hello, {player_name}! Let's play Battleship.")

    # Create player and computer boards
    player_board = Board()
    computer_board = Board()

    # Place ships on the boards
    player_board.place_ship()
    computer_board.place_ship()

    # Display the boards
    print(f"\n{player_name}'s Board:")
    player_board.display(show_ships=True)
    print("\nComputer's Board:")
    computer_board.display(show_ships=False)

    while True:

        while True:
            col = input("\nEnter a column (A-H): ").upper()
            if player_board.valid_cl(col):
                break
            else:
                print("Invalid column. You must choose between (A-H).")
                print("Please try again.")

        while True:
            row = input("\nEnter a row (1-8): ")
            if player_board.valid_rw(row):
                break
            else:
                print("Invalid row. You must choose between (1-8).")
                print("Please try again.")

        print(f"Your choice is: {col}{row}")


# Call the new_game function to start the game
new_game()
