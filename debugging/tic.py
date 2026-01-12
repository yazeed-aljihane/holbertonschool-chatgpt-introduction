#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("-" * 11)

def check_winner(board):
    # فحص الصفوف
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    # فحص الأعمدة
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    # فحص الأقطار
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Error: Out of bounds! Range is 0-2.")
                continue
                
            if board[row][col] != " ":
                print("Error: Spot already taken!")
                continue
                
            board[row][col] = current_player
            
            if check_winner(board):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break
                
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
                
            # تغيير اللاعب فقط بعد التأكد من عدم الفوز
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    tic_tac_toe()
