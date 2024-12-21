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



if __name__ == '__main__':

    # Read in file with elements to sort
    capital_cities = get_list_to_sort()
    print(f"Number of cities to sort : {len(capital_cities)}")
