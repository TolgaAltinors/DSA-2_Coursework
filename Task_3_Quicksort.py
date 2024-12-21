import os

# Store the directory we are in
current_dir = os.getcwd()
print (current_dir)

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
    full_path = os.path.join(current_dir, file_name)
    
    # Create list to hold the data
    capital_cities = []
    
    # Open the file and read contents into list
    with open(full_path, 'r') as f:
        for line in f:
            capital_cities.append(line.strip())
                
    return capital_cities


"""
1 - ADD FUNCTION TO RETURN PARTITION INDEX

    Function signature:
        array to sort
        start index
        end index
        
        pivot_index := len(array) - 1 (Select second to last element)
        pivot       := array[pivot_index]
    
        (swap last 2 elements around and make the pivot the last in array)
        swap array[pivot_index] with array[end_index]
    
        i := start_index - 1
    
        for j := 0 to len(array) do
            if array[j] < pivot then
                swap array[i] with array[j]
                
                i := i + 1 (Move the pivot index over by one)

        swap array[i + 1] with array[end_index]
    
        return i + 1 (new pivot)
    
    
2 - ADD QUICK SORT FUNCTION

    Function signature:
        array to sort
        start index
        end index
        
        if start_index < end_index then
        
        pivot_index := call partition function (array, start_index, end_index)
        
        quicksort(array, start_index, pivot_index - 1)
        quicksort(array, pivot_index + 1, end_index)
        
3 - ADD FUNCTION TO READ IN FILE

"""

def quicksort(list_to_sort, start = 0, end = None):
    
    print(f"Number of cities to sort : {len(list_to_sort)}")
    print(f"Sublist : {list_to_sort}")
    
    if end == None:
        end = len(list_to_sort) - 1
    
    if start < end:

        pivot_index = create_sublist(list_to_sort, start, end)

        print("")
        print(f"Number of cities to sort : {len(list_to_sort[start:pivot_index])}")
        print(f"Sublist : {list_to_sort[start:pivot_index]}")


def create_sublist(sub_list, start, end):

    # set pivot to be the second to last element
    pivot_index = end - 1
    
    # pivot represent the value we are comparing against
    pivot = sub_list[pivot_index]
    
    print(f"Pivot index : {pivot_index}")
    print(f"Pivot value : {pivot}")

    sub_list[pivot_index], sub_list[end] = sub_list[end], sub_list[pivot_index]  # Move pivot to end
    
    # variable to track new pivot position
    i = start - 1

    for j in range(start, end):

        if (sub_list[j] > pivot):
            print(f"FALSE --> {sub_list[j]} > {pivot} --> NO SWAP")

        if sub_list[j] <= pivot:
            # Increment pivot position
            i += 1
            
            if sub_list[i] != sub_list[j]:
                print(f" TRUE --> {sub_list[j]} <= {pivot} --> SWAP")
                sub_list[i], sub_list[j] = sub_list[j], sub_list[i]
    
    # move the pivot to the right place        
    sub_list[i + 1], sub_list[end] = sub_list[end], sub_list[i + 1]
    
    return i + 1



if __name__ == '__main__':

    # Read in file with elements to sort
    capital_cities = get_list_to_sort()
    print(f"Number of cities to sort : {len(capital_cities)}")
    
    quicksort(capital_cities)
    
