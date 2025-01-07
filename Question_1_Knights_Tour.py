import numpy as np

from open_backtracking import open_backtracking_knights_tour
from closed_backtracking import closed_backtracking_knights_tour
from open_lasVegas import open_lasVegas_knights_tour
from closed_lasVegas import closed_lasVegas_knights_tour


# possible moves for the knight (L shape)
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

# create the chess board
row_count = 8
col_count = 8
chess_board = np.zeros((row_count, col_count))

# set starting position
chess_board[0, 0] = 1

print(chess_board)

# Dictionary to hold descriptions
keys = {'O' : 'Open',
        'C' : 'Closed',
        'B' : 'Backtracking',
        'L' : 'Las Vegas'}

# Check to see whether position is a valid one
def check_move_on_board(brd, row, col):
    
    # validate row position
    good_row = row >= 0 and row < row_count
    # validate column position
    good_col = col >= 0 and col < col_count
    # Have we visited the cell before
    not_visited = False
    if brd[row,col] == 0:
        not_visited = True
    
    if good_row and good_col and not_visited:
        
        return True
    

if __name__=="__main__":

#   Initialise variables
    OpenOrClose = 'O'
    BacktrackOrLasVegas = 'B'
    
    # If user enters an invalid choice the deaults above will be used
    user_response = input("Choose 'Open' or 'Close' version for Knight's Tour? Type 'O' (Open) or 'C' (Close). ")
    if user_response in ('O', 'C'):
        OpenOrClose = user_response
        
    user_response = input("Choose 'Backtracking' or 'Las Vegas' approach for Knight's Tour? Type 'B' (Backtracking) or 'L' (Las Vegasose). ")
    if user_response in ('B', 'L'):
        BacktrackingOrLasVegas = user_response

    # print(f"User selected the '{keys[OpenOrClose]}' version and '{keys[BacktrackOrLasVegas]}' approach for the Knight's tour.")
    
    if OpenOrClose == "O":
        
        if BacktrackingOrLasVegas == 'B':
            open_backtracking_knights_tour(chess_board, 0, 0)
        else:
            open_lasVegas_knights_tour()

    elif OpenOrClose == 'C':

        if BacktrackingOrLasVegas == 'B':
            closed_backtracking_knights_tour()
        else:
            closed_lasVegas_knights_tour()
        
    
    check_move_on_board(chess_board, 2, 7)