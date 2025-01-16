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


def find_knights_tour(user_response):

    attempt_count = 300000

    best_effort = 0
    best_chess_board = np.zeros((row_count, col_count))

    # store original start position for checking closed tour
    start_x, start_y = 0, 0
    
    for attempts in range(attempt_count):
        
        # initialise board
        chess_board = np.zeros((row_count, col_count))
        
        # get random start position        
        x = random.randint(0, row_count - 1)
        y = random.randint(0, col_count - 1)
        chess_board[x][y] = 1
        
        # max moves we can make
        max_moves = row_count * col_count
        
        # Move start from 2 as staring position set to 1
        for num_of_moves in range(2, max_moves):
            
            # store possible moves in list
            stored_moves=[]
            
            # find possible moves by adding what's x_y_moves to current x and y
            for x_move, y_move in x_y_moves:
                
                new_x, new_y = x + x_move, y + y_move
                
                # check if it is a valid move
                if check_move_on_board(chess_board, new_x, new_y):
                    stored_moves.append((new_x, new_y))

            # break condition
            if len(stored_moves) == 0:
                
                if num_of_moves > best_effort:
                    best_effort = num_of_moves
                    best_chess_board = chess_board
                    # store original start position for checking closed tour
                    start_x, start_y = x, y
                break
            
            # select a random x, y from stored_moves and update chess board
            new_x, new_y = random.choice(stored_moves)
            chess_board[new_x][new_y] = num_of_moves
            
            # set x, y to latest position
            x, y = new_x, new_y
            # print(f"X = {new_x} --- Y = {new_y}")
            # print(chess_board)
        
            # check if we found a vaild tour
            if num_of_moves == max_moves:

                # Open Knight's tour, return the chess board
                if user_response == 3:
                    return True, chess_board

                # Closed Knight's tour - check if can reach the start position
                elif user_response == 4:
                    # Get starting postion from chess board
                    start_pos = np.argwhere(chess_board == 1)
                    start_x, start_y = start_pos[0][0], start_pos[0][1]

                    # We know the last position - x and y
                    # Find all possible moves from here

                    # Check to see whether original start position is one of them


    print(f"**** {attempts + 1} attempts were made to find a knight's tour")
    print()
    print(f"**** Closest we got was {best_effort - 1} moves.")
    print()
    start_pos = np.argwhere(best_chess_board == 1)
    print(f"**** Start x = {start_pos[0][0]} --- Start y = {start_pos[0][1]}.")
        
    return None, best_chess_board


def lasVegas_knights_tour(user_response):
    
    if user_response == 3:
        print("**************************************")
        print("*** Open knight's tour using Las Vegas")
        print("**************************************")
    elif user_response == 4:
        print("****************************************")
        print("*** Closed knight's tour using Las Vegas")
        print("****************************************")

    succsess, board = find_knights_tour(user_response)

    if succsess:
        print()
        print("*** Found a valid tour ***")
        print()
    else:
        print()
        print("*** Failed to find a valid tour ***")
        print()
    
    print(board)
    