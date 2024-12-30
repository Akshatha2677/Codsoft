def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    # Winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_full(board):
    return all(cell in ('X', 'O') for cell in board)

def tic_tac_toe():
    board = [' '] * 9  # Initialize the board with empty spaces
    current_player = 'X'
    
    print("Tic-Tac-Toe Game!")
    print_board(board)
    
    while True:
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError("Invalid move. Enter a number between 1 and 9.")
            if board[move] != ' ':
                raise ValueError("The cell is already occupied.")
        except ValueError as e:
            print(e)
            continue
        
        # Make the move
        board[move] = current_player
        print_board(board)
        
        # Check for a win or draw
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
