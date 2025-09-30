import os, time, random, sys

try:
    import msvcrt  # Windows
    WINDOWS = True
except ImportError:
    import termios, tty, select  # Linux/Mac
    WINDOWS = False

from utilities import TetrisUtils   # your helper class


def get_key():
    """Non-blocking key reader."""
    if WINDOWS:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            return ch.decode().lower()
        return None
    else:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1).lower()
        return None


def main():
    game = TetrisUtils()
    board = game.create_board()
    score = 0
    game_over = False

    while not game_over:
        piece = game.get_random_tetro_min()
        pos_row, pos_col = 0, game.cols // 2 - len(piece[0]) // 2

        if not game._valid_position(piece, (pos_row, pos_col), board):
            print("GAME OVER! Final Score:", score)
            break

        falling = True
        last_fall = time.time()
        gravity = 1.0  # seconds between falls (decrease for difficulty)

        while falling:
            # render
            os.system("cls" if os.name == "nt" else "clear")
            print("Score:", score)
            temp_board = game.draw_board_with_piece(board, piece, (pos_row, pos_col))
            game.draw_board(temp_board)

            # input
            print("Move (a=left, d=right, s=down, w=rotate, space=drop, q=quit)")
            key = get_key()
            if key == "q":
                game_over = True
                break
            elif key == "a":  # left
                if game._valid_position(piece, (pos_row, pos_col - 1), board):
                    pos_col -= 1
            elif key == "d":  # right
                if game._valid_position(piece, (pos_row, pos_col + 1), board):
                    pos_col += 1
            elif key == "s":  # soft drop
                if game._valid_position(piece, (pos_row + 1, pos_col), board):
                    pos_row += 1
                    last_fall = time.time()  # reset gravity timer
                else:
                    falling = False
            elif key == " ":  # hard drop
                while game._valid_position(piece, (pos_row + 1, pos_col), board):
                    pos_row += 1
                falling = False
            elif key == "w":  # rotate
                piece = game.try_rotate(piece, (pos_row, pos_col), board)

            # gravity auto drop
            if time.time() - last_fall >= gravity:
                if game._valid_position(piece, (pos_row + 1, pos_col), board):
                    pos_row += 1
                else:
                    falling = False
                last_fall = time.time()

            time.sleep(0.05)  # small delay to avoid high CPU usage

        # lock piece
        if not game_over:
            game.lock_piece(board, piece, (pos_row, pos_col))
            board, cleared = game.clear_full_rows(board)
            score += game.calculate_score(cleared)




welcome_text = r"""
                                 created by: ARUN ARUNISTO
___________________________________________.___  _________
\__    ___/\_   _____/\__    ___/\______   \   |/   _____/
  |    |    |    __)_   |    |    |       _/   |\_____  \ 
  |    |    |        \  |    |    |    |   \   |/        \
  |____|   /_______  /  |____|    |____|_  /___/_______  /
                   \/                    \/            \/ 
"""
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(welcome_text)
    options = input("[1] Start the Game [2] Exit\nEnter the option: ")
    if options == "1":
        if not WINDOWS:
            # configure terminal for Linux/Mac
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(fd)
                main()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        else:
            main()
    elif options == "2":
        print("Thank You for playing! 👋")
    else:
        print("Invalid option. Please choose 1 or 2.")
