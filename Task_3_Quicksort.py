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