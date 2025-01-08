import numpy as np
import helpers

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

# Check to see whether position is a valid one
# Is the row, col position within the board's boundary
# Has the row, col position previously been visited
def check_move_on_board(brd, row, col):
    
    # validate row position
    good_row = row >= 0 and row < row_count

    # validate column position
    good_col = col >= 0 and col < col_count

    # Have we visited the cell before
    if good_row and good_col and brd[row, col] == 0:
        return True


# The recursive function that will find the next moves
def find_knights_tour(chess_board, curr_x, curr_y, num_of_moves=1):

    # set the bas case for exiting  
    if num_of_moves == max_moves:
        return True
    
    # Loop around the size of the board looking for the next move
    for i in range(board_size):
    
        next_x = curr_x + x_moves[i]
        next_y = curr_y + y_moves[i]
        
        # If the new positions are valid
        if check_move_on_board(chess_board, next_x, next_y):
            
            # update the cell with the movement counter
            chess_board[next_x][next_y] = num_of_moves
            
            if find_knights_tour(chess_board, next_x, next_y, num_of_moves+1):
                return True
        
            # Set back to zero as not successful 
            chess_board[next_x][next_y] = 0
    return False


def open_backtracking_knights_tour():
    
    if find_knights_tour(chess_board, 0, 0):
        print("*** Found a valid tour ***")
        print(chess_board)

    else:
        print("*** Failed to find a valid tour ***")

