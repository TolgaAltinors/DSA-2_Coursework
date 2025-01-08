
from closed_backtracking import closed_backtracking_knights_tour
from open_lasVegas import open_lasVegas_knights_tour
from closed_lasVegas import closed_lasVegas_knights_tour


# Dictionary to hold descriptions
keys = {'O' : 'Open',
        'C' : 'Closed',
        'B' : 'Backtracking',
        'L' : 'Las Vegas'}


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
            from open_backtracking import open_backtracking_knights_tour

            open_backtracking_knights_tour()
        else:
            open_lasVegas_knights_tour()

    elif OpenOrClose == 'C':

        if BacktrackingOrLasVegas == 'B':
            closed_backtracking_knights_tour()
        else:
            closed_lasVegas_knights_tour()
