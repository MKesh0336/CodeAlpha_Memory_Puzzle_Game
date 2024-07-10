import random
import time
import os

# Initialize the cards
cards = list('AABBCCDDEEFFGGHH')
random.shuffle(cards)

# Create the game board
board = [['' for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j] = cards.pop()

# Function to display the board
def display_board(board, mask):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  1 2 3 4")
    for i in range(4):
        print(f"{i+1} ", end='')
        for j in range(4):
            if mask[i][j]:
                print(board[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

# Initialize mask for board
mask = [[False for _ in range(4)] for _ in range(4)]

# Function to check if the game is won
def check_win(mask):
    for row in mask:
        if False in row:
            return False
    return True

# Game loop
while True:
    display_board(board, mask)
    if check_win(mask):
        print("Congratulations! You've matched all pairs!")
        break

    # Get user input
    try:
        row1, col1 = map(int, input("Enter the first card position (row and column): ").split())
        row2, col2 = map(int, input("Enter the second card position (row and column): ").split())
    except ValueError:
        print("Invalid input. Please enter row and column numbers.")
        time.sleep(2)
        continue

    # Convert to 0-based indexing
    row1, col1, row2, col2 = row1-1, col1-1, row2-1, col2-1

    if (row1 == row2 and col1 == col2) or mask[row1][col1] or mask[row2][col2]:
        print("Invalid positions. Try again.")
        time.sleep(2)
        continue

    # Reveal the cards
    mask[row1][col1] = True
    mask[row2][col2] = True
    display_board(board, mask)
    time.sleep(2)

    # Check if the cards match
    if board[row1][col1] != board[row2][col2]:
        mask[row1][col1] = False
        mask[row2][col2] = False

    display_board(board, mask)
