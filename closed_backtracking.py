import numpy as np
import helpers
from helpers import check_move_on_board

# Initialise some variables
x_moves = helpers.get_x_moves()
y_moves = helpers.get_y_moves()

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

def closed_backtracking_knights_tour():
    
    print("Closed knight's tour using backtracking")
    print("NOT YET IMPLEMENTED")
    
    zip_lists = helpers.zip_x_y_moves()
    print(zip_lists)
