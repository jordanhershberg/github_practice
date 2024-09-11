def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    return any(all(board[i] == mark for i in condition) for condition in win_conditions)

def is_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def play_round():
    board = [' ']*9
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Choose a number between 1 and 9.")
                continue
            if board[move] != ' ':
                print("This cell is already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return current_player
        
        if is_full(board):
            print_board(board)
            print("The game is a draw!")
            return 'D'  # Draw
        
        current_player = 'O' if current_player == 'X' else 'X'

def tic_tac_toe():
    scores = {'X': 0, 'O': 0}
    rounds_played = 0
    
    while rounds_played < 3:
        print(f"\nRound {rounds_played + 1}")
        result = play_round()
        
        if result != 'D':
            scores[result] += 1
        
        rounds_played += 1
        
        print(f"Scores: Player X: {scores['X']}, Player O: {scores['O']}")
        
        if rounds_played < 3:
            play_again = input("Do you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                break
    
    if scores['X'] > scores['O']:
        print("Player X is the overall winner!")
    elif scores['O'] > scores['X']:
        print("Player O is the overall winner!")
    else:
        print("The game is a draw overall!")

if __name__ == "__main__":
    tic_tac_toe()