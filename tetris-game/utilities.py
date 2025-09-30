import random
import copy
class TetrisUtils:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.shapes = [
                        [[1, 1, 1, 1]],                  # I
                        [[1, 1], [1, 1]],                # O
                        [[0, 1, 0], [1, 1, 1]],          # T
                        [[1, 0, 0], [1, 1, 1]],          # J
                        [[0, 0, 1], [1, 1, 1]],          # L
                        [[0, 1, 1], [1, 1, 0]],          # S
                        [[1, 1, 0], [0, 1, 1]],          # Z
                    ]
        self.score_map = {
                    1: 100,
                    2: 300,
                    3: 500,
                    4: 800
                }
    def _valid_position(self, piece, position, board):
        pos_row, pos_col = position # where the top-left corner of piece should go

        for row in range(len(piece)):
            for col in range(len(piece[row])):
                if piece[row][col] == 1: # block exists here
                    board_row = pos_row + row
                    board_col = pos_col + col

                    # 1. check boundaries
                    if board_row < 0 or board_row >= self.rows:
                        return False
                    if board_col < 0 or board_col >= self.cols:
                        return False
                    
                    # checking collision with filled board cell
                    if board[board_row][board_col] == 1:
                        return False
        return True
    
    def _rotate_tetro(self, tetro):
        new_piece = []
        for col in range(len(tetro[0])):
            new_row = []
            for row in reversed(range(len(tetro))):
                new_row.append(tetro[row][col])
            new_piece.append(new_row)
        return new_piece

    def create_board(self):
        board = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                row.append(0)
            board.append(row)
        return board
    
    def draw_board(self, board):
        for row in board:
            print("|", end="")
            for cell in row:
                if cell == 0:
                    print("  ", end="") # empty
                else:
                    print("[]", end="")# filled
            print("|")
    
    def get_random_tetro_min(self):
        return random.choice(self.shapes)
    
    def try_rotate(self, piece, position, board):
        rotated_piece = self._rotate_tetro(piece)
        if self._valid_position(rotated_piece, position, board):
            return rotated_piece
        else:
            return piece
    
    def draw_board_with_piece(self, board, piece, position):
        pos_row, pos_col = position
        temp_board = copy.deepcopy(board)

        for row in range(len(piece)):
            for col in range(len(piece[row])):
                if piece[row][col] == 1:
                    board_row = pos_row + row
                    board_col = pos_col + col

                    # only draw inside visible area
                    if 0 <= board_row < self.rows and 0 <= board_col < self.cols:
                        temp_board[board_row][board_col] = 1
        return temp_board
    
    def lock_piece(self, board, piece, position):
        pos_row, pos_col = position

        for row in range(len(piece)):
            for col in range(len(piece[row])):
                if piece[row][col] == 1:
                    board_row = pos_row+row
                    board_col = pos_col + col
                    board[board_row][board_col] = 1 #permanently place
    
    def clear_full_rows(self, board):
        new_board = []
        cleared_rows = 0
        for row in board:
            if all(cell == 1 for cell in row): # row is full:
                cleared_rows += 1
            else:
                new_board.append(row)
        
        # adding empty rows
        empty_rows = [[0]* self.cols for _ in range(cleared_rows)]
        new_board = empty_rows + new_board
        
        return new_board, cleared_rows
    
    def calculate_score(self, cleared_rows):
        return self.score_map.get(cleared_rows, 0)

    
    
    
