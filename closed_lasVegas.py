import random
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



def find_knights_tour():

    attempt_count = 10000

    best_effort = 0
    best_chess_board = np.zeros((row_count, col_count))

    
    for attempts in range(attempt_count):
        
        # initialise board
        chess_board = np.zeros((row_count, col_count))
        
        # get random start position        
        x = random.randint(0, row_count - 1)
        y = random.randint(0, col_count - 1)
        
        max_moves = row_count * col_count
        
        for num_of_moves in range(1, max_moves):
            
            # store possible moves in list
            stored_moves=[]
            
    pass




def closed_lasVegas_knights_tour():
    
    print("Closed knight's tour using Las Vegas")
    print("NOT YET IMPLEMENTED")