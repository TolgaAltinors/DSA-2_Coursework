

# Dictionary to hold descriptions
keys = {1 : 'Back tracking - Open',
        2 : 'Back tracking - Closed',
        3 : 'Las Vegas - Open',
        4 : 'Las Vegas - Closed'}


if __name__=="__main__":

    print("Please select from one of the options for the knight's tour. Type corresponding number.")
    for k, v in keys.items():
        print(f"{k} - {v}")
    user_response = int(input("... "))

    if user_response == 1:
        from open_backtracking import open_backtracking_knights_tour
        open_backtracking_knights_tour()
        
    elif user_response == 2:
        from closed_backtracking import closed_backtracking_knights_tour
        closed_backtracking_knights_tour()

    elif user_response == 3 or user_response == 4:
        from lasVegas import lasVegas_knights_tour
        lasVegas_knights_tour(user_response)
    else:
        print("Number entered not matched to the option given")

