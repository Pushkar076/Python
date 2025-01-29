def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Columns
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):  # Diagonals
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter positions (1-9) as shown below:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    while True:
        print_board(board)
        try:
            position = int(input(f"Player {current_player}, enter position (1-9): "))
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        row = (position - 1) // 3
        col = (position - 1) % 3
        
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("That position is already taken!")
            continue
            
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()