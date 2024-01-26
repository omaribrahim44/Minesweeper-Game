import random

def initialize_board(rows, cols, num_mines):
    # Create a blank Minesweeper board
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly on the board
    for _ in range(num_mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == '*':
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = '*'

    return board

def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if board[i][j] == '*':
                count += 1
    return count

def reveal(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == ' ':
        mines = count_adjacent_mines(board, row, col)
        board[row][col] = str(mines) if mines > 0 else ' '
        if mines == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    reveal(board, i, j)

def play_game(rows, cols, num_mines):
    board = initialize_board(rows, cols, num_mines)
    game_over = False

    while not game_over:
        display_board(board)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))

        if board[row][col] == '*':
            print("Game Over! You hit a mine.")
            game_over = True
        else:
            reveal(board, row, col)
            if all(cell != ' ' for row in board for cell in row if cell != '*'):
                print("Congratulations! You've won!")
                game_over = True

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    num_mines = int(input("Enter the number of mines: "))
    
    play_game(rows, cols, num_mines)
