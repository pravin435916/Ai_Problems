def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('--' * 5)

def get_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def play_game():
    board = create_board()
    current_player = 'X'
    winner = None

    while winner is None:
        print_board(board)
        print(f"It's player {current_player}'s turn.")

        valid_move = False
        while not valid_move:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = current_player
                valid_move = True
            else:
                print("Invalid move! Try again.")

        winner = get_winner(board)
        if winner is None:
            current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print(f"Player {winner} wins!")

play_game()
