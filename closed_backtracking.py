import numpy as np
import helpers
from helpers import check_move_on_board

# Initialise some variables
x_moves = helpers.get_x_moves()
y_moves = helpers.get_y_moves()

x_y_moves = helpers.zip_x_y_moves()

# create the chess board
row_count = helpers.get_row_count()
col_count = helpers.get_col_count()

chess_board = np.zeros((row_count, col_count))

# DETERMINE MAXIMUM MOVEMENT COUNT AS A BASE CASE    
board_size = len(chess_board)
max_moves = board_size * board_size

print()
print("*** Starting board ***")
print(chess_board)
print()

# Define possible moves by current x and y
def possible_moves(x, y):
    knights_moves = []
    for add_x, add_y in x_y_moves:
        knights_moves.append((x + add_x, y + add_y))
    return knights_moves


def find_knights_tour(board, x, y):
    
    knights_moves = possible_moves(x, y)


def closed_backtracking_knights_tour():
    
    print("Closed knight's tour using backtracking")
    print("NOT YET IMPLEMENTED")
    
    find_knights_tour(chess_board, x=0, y=0)