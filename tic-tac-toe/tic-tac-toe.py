import time

# Winning combinations
WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]              # diagonals
]

def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def make_move(move, player, board):
    if board[move] != " ":
        raise Exception("Invalid move")
    board[move] = player

def check_win(board, player):
    for line in WIN_LINES:
        if all(board[i] == player for i in line):
            return True
    return False

def find_the_empty(board):
    return [i + 1 for i in range(len(board)) if board[i] == " "]

def check_draw(board):
    return " " not in board

def computer_move(board, computer, player):
    # 1. Try to win
    for line in WIN_LINES:
        values = [board[i] for i in line]
        if values.count(computer) == 2 and values.count(" ") == 1:
            move = line[values.index(" ")]
            make_move(move, computer, board)
            return

    # 2. Try to block opponent
    for line in WIN_LINES:
        values = [board[i] for i in line]
        if values.count(player) == 2 and values.count(" ") == 1:
            move = line[values.index(" ")]
            make_move(move, computer, board)
            return

    # 3. Take center
    if board[4] == " ":
        make_move(4, computer, board)
        return

    # 4. Take corner
    for move in [0, 2, 6, 8]:
        if board[move] == " ":
            make_move(move, computer, board)
            return

    # 5. Take side
    for move in [1, 3, 5, 7]:
        if board[move] == " ":
            make_move(move, computer, board)
            return

def game_logic(computer, player):
    board = [" "] * 9
    print_board(board)

    while True:
        remaining_columns = find_the_empty(board)
        move_from_player = input(f"Select a move from {remaining_columns}: ")
        try:
            if int(move_from_player) in remaining_columns:
                make_move(int(move_from_player)-1, player, board)
                print_board(board)
                if check_win(board, player):
                    print("You won!! 🎉")
                    break
                elif check_draw(board):
                    print("Draw!! 🤝")
                    break
            else:
                print("Invalid move! Choose from:", remaining_columns)
                continue
        except Exception:
            print("Invalid input! Please enter a number.")

        print("Computer's turn...")
        time.sleep(1)
        computer_move(board, computer, player)
        print_board(board)
        if check_win(board, computer):
            print("Computer won!! 🤖")
            break
        elif check_draw(board):
            print("Draw!! 🤝")
            break

def play_game():
    computer = "X"
    player = "O"
    while True:
        options = input("[1] Start the Game [2] Quit the Game\nEnter the option: ")
        if options == "1":
            game_logic(computer, player)
        elif options == "2":
            print("Thank You for playing! 👋")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

welcome_text = r"""
                                                                            Created by: ARUN ARUNISTO
___________.____________         ________________  _________         ___________________  ___________
\__    ___/|   \_   ___ \        \__    ___/  _  \ \_   ___ \        \__    ___/\_____  \ \_   _____/
  |    |   |   /    \  \/   ______ |    | /  /_\  \/    \  \/   ______ |    |    /   |   \ |    __)_ 
  |    |   |   \     \____ /_____/ |    |/    |    \     \____ /_____/ |    |   /    |    \|        \
  |____|   |___|\______  /         |____|\____|__  /\______  /         |____|   \_______  /_______  /
                       \/                        \/        \/                           \/        \/ 

"""
if __name__ == "__main__":
    print(welcome_text)
    play_game()
