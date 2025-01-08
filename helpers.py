# This probably is not the best way of doing this but I thought
# since these will be used in all versions I would store them here

# possible moves for the knight (L shape)
def get_x_moves():
    return [2, 1, -1, -2, -2, -1, 1, 2]

def get_y_moves():
    return [1, 2, 2, 1, -1, -2, -2, -1]

# Set row and column counts
def get_row_count():
    return 8

def get_col_count():
    return 8
