"""Import randint from random module"""
from random import randint

import os


class Board:
    """Game board for Battleship class. Sets board size, the player's name,
    and displays the boards for both the player and computer.
    Checks if the moves for both sides were a hit or miss, and
    displays it on the game board.
    """

    def __init__(self, size=8):
        self.size = size
        self.grid = [[' '] * size for _ in range(size)]
        self.row_labels = [str(i+1) for i in range(size)]
        self.col_labels = 'ABCDEFGH'
        self.player_hits = 0
        self.computer_hits = 0

    def display(self, show_ships=False):
        """Print the board with row and column labels.
        """
        print('  ' + ' '.join(self.col_labels))
        for idx, row in enumerate(self.grid):
            display_row = [cell if (cell == ' ' or show_ships
                                    or cell in ['*', 'X'])
                           else ' ' for cell in row]
            print(self.row_labels[idx] + '|' + '|'.join(display_row) + '|')

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
        """Checks if the player's column choice is valid.
        """
        return col in self.col_labels

    def valid_rw(self, row):
        """Checks if the player's row choice is valid.
        """
        return row in self.row_labels

    def check_move(self, col_index, row_index):
        """Checks if the player's and computer's move is a hit or miss.
        """
        return self.grid[row_index][col_index] == '@'

    def mark_move(self, col_index, row_index, hit):
        """Marks the player's and computer's move on the board.
        """
        if hit:
            self.grid[row_index][col_index] = '*'
        else:
            self.grid[row_index][col_index] = 'X'

    def all_ships_sunk(self):
        """Checks if all the ships have been sunk.
        """
        for row in self.grid:
            if '@' in row:
                return False
        return True


def clear_scr():
    """Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def new_game():
    """New game function.
    Starts a new game of Battleship.
    """
    print("Welcome to my Battleship game!")

    # Loop to ensure that the player enters a name
    while True:
        player_name = input("What is your name?\n").strip()
        if player_name:
            break
        else:
            print("You must enter a name. Please try again.")
    print("\n")
    print(f"Hello, {player_name}! Let's play Battleship.")

    # Create player and computer boards
    player_board = Board()
    computer_board = Board()

    # Place ships on the boards
    player_board.place_ship()
    computer_board.place_ship()

    # Display the boards
    print("'@' is for ships, "
          "'X' is a miss, and '*' is a hit.")
    print(f"\n{player_name}'s Board:")
    player_board.display(show_ships=True)
    print("\nComputer's Board:")
    computer_board.display(show_ships=False)

    player_moves = set()

    while True:

        while True:
            col = input("\nEnter a column (A-H):\n").strip().upper()
            if col and player_board.valid_cl(col):
                break
            else:
                print("Invalid column choice. You must choose between (A-H).")
                print("Please try again.")

        while True:
            row = input("\nEnter a row (1-8):\n")
            if player_board.valid_rw(row):
                break
            else:
                print("Invalid row choice. You must choose between (1-8).")
                print("Please try again.")

        move = (col, row)
        if move in player_moves:
            print("This move has already been made. Please try again.")
            continue

        player_moves.add(move)

        # Clear the screen
        clear_scr()

        print(f"Your choice is: {col}{row}.")

        col_index = player_board.col_labels.index(col)
        row_index = player_board.row_labels.index(row)

        # Check if the player's move is a hit or miss
        player_hit = computer_board.check_move(col_index, row_index)
        computer_board.mark_move(col_index, row_index, player_hit)
        if player_hit:
            player_board.player_hits += 1

        # Computer's turn
        while True:
            comp_cl_index = randint(0, computer_board.size - 1)
            comp_rw_index = randint(0, computer_board.size - 1)
            if player_board.grid[comp_rw_index][comp_cl_index] not in [
                    'X', '*']:
                break

        # Check if the computer's move is a hit or miss
        computer_hit = player_board.check_move(comp_cl_index, comp_rw_index)
        player_board.mark_move(comp_cl_index, comp_rw_index, computer_hit)
        if computer_hit:
            computer_board.computer_hits += 1

        comp_cl = computer_board.col_labels[comp_cl_index]
        comp_rw = computer_board.row_labels[comp_rw_index]

        print(f"Computer's choice is: {comp_cl}{comp_rw}.")
        print(f"\n{player_name}'s move was a hit!" if player_hit
              else f"\n{player_name}'s move was a miss.")
        print("Computer's move was a hit!" if computer_hit
              else "Computer's move was a miss.")

        # Display the current score
        print(f"\n{player_name}'s score: {player_board.player_hits}"
              f" - Computer's score: {computer_board.computer_hits}")

        # Display the boards after each move
        print(f"\n{player_name}'s Board:")
        player_board.display(show_ships=True)
        print("\nComputer's Board:")
        computer_board.display(show_ships=False)

        # Check for end game conditions
        if computer_board.all_ships_sunk():
            print(f"\nCongratulations {player_name}!")
            print("You have sunk all the computer's ships!")
            print("You win!")
            print(f"\nThe final score is: {player_name}:"
                  f"{player_board.player_hits}"
                  f" - Computer: {computer_board.computer_hits}")
            break

        if player_board.all_ships_sunk():
            print("\nAhhh! Darn it!")
            print("The computer has sunk all your ships!")
            print("You lose!")
            print(f"\nThe final score is: {player_name}:"
                  f"{player_board.player_hits}"
                  f" - Computer: {computer_board.computer_hits}")
            break


# Call the new_game function to start a new game
new_game()
