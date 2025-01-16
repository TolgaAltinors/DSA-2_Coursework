# This probably is not the best way of doing this but I thought
# since these will be used in all versions I would store them here

# possible moves for the knight (L shape)
def get_x_moves():
    return [2, 1, -1, -2, -2, -1, 1, 2]

def get_y_moves():
    return [1, 2, 2, 1, -1, -2, -2, -1]

def zip_x_y_moves():
    return [[x, y] for x, y in zip(get_x_moves(), get_y_moves())]

# Set row and column counts
def get_row_count():
    return 8

def get_col_count():
    return 8


# Check to see whether position is a valid one
# Is the row, col position within the board's boundary
# Has the row, col position previously been visited
def check_move_on_board(brd, row, col):
    
    # validate row position
    good_row = row >= 0 and row < get_row_count()

    # validate column position
    good_col = col >= 0 and col < get_col_count()

    # Have we visited the cell before
    if good_row and good_col and brd[row, col] == 0:
        return True
