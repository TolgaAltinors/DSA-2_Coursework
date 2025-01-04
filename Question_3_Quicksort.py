import os
import time
from pathlib import Path

# Get directory to read/write file
script_fullpath = os.path.abspath(__file__)  
script_path = os.path.dirname(script_fullpath)  

def get_list_to_sort() -> list :
    """ Read in file from current directory and return a list
        Arguments:
            None
        Returns:
            {list} -- list of words
    """
    # Read in file with list of cities - file is in the same location as script
    file_name = "List_of_Cities.txt"
    
    # Build the path for the text file
    full_path = os.path.join(script_path, file_name)
    
    # Create list to hold the data
    capital_cities = []
    
    # Open the file and read contents into list
    with open(full_path, 'r') as f:
        for line in f:
            capital_cities.append(line.strip())
                
    return capital_cities


def output_to_console(list_to_output):
    
    for ind, city in enumerate(list_to_output):
        print(f"{ind+1:03} - {city}")    

def output_to_file(capital_cities):
    out_file = "List_of_Cities_Sorted.txt"
    full_path = os.path.join(script_path, out_file)

    with open(full_path, 'w') as f:
            for line in capital_cities:
                f.write(line + '\n')
    print (f"File output to: {full_path}")

def quicksort(list_to_sort, start = 0, end = None):
    
    # print(f"Number of cities to sort : {len(list_to_sort)}")
    # print(f"Sublist : {list_to_sort}")
    
    # first time we call quicksort
    if end == None:
        end = len(list_to_sort) - 1
    
    if start < end:

        pivot_index = create_sublist(list_to_sort, start, end)

        # print("")
        # print(f"Number of cities to sort : {len(list_to_sort[start:pivot_index])}")
        # print(f"Sublist : {list_to_sort[start:pivot_index]}")
        
        quicksort(list_to_sort, start, pivot_index - 1)
        quicksort(list_to_sort, pivot_index + 1, end)


def create_sublist(sub_list, start, end):

    # set pivot to be the second to last element
    pivot_index = end - 1
    
    # pivot represent the value we are comparing against
    pivot = sub_list[pivot_index]
    
    # print(f"Pivot index : {pivot_index}")
    # print(f"Pivot value : {pivot}")

    sub_list[pivot_index], sub_list[end] = sub_list[end], sub_list[pivot_index]  # Move pivot to end
    
    # variable to track new pivot position
    i = start - 1

    for j in range(start, end):

        # if (sub_list[j] > pivot):
        #     print(f"FALSE --> {sub_list[j]} > {pivot} --> NO SWAP")

        if sub_list[j] <= pivot:
            # Increment pivot position
            i += 1
            
            if sub_list[i] != sub_list[j]:
                # print(f" TRUE --> {sub_list[j]} <= {pivot} --> SWAP")
                sub_list[i], sub_list[j] = sub_list[j], sub_list[i]
    
    # move the pivot to the right place        
    sub_list[i + 1], sub_list[end] = sub_list[end], sub_list[i + 1]
    
    # Return pivot position
    return i + 1


if __name__ == '__main__':

    # Read in file with elements to sort
    capital_cities = get_list_to_sort()
    print(f"Number of cities to sort : {len(capital_cities)}")
    
    quicksort(capital_cities)
    
    # Output return from quick sort and print to console
    user_response = input("Display output to console or output to file? Type 'D' (Display) or 'O' (Output). ")
    
    if user_response == 'D':
        output_to_console(capital_cities)

    elif user_response == 'O':
        output_to_file(capital_cities)

    else:
        print("*******************")
        print(f"*** User response '{user_response}' not recognised. ***")
        print(f"*** Outputting to file and console. ***")
        print("*******************")
        time.sleep(2)
        output_to_console(capital_cities)
        output_to_file(capital_cities)