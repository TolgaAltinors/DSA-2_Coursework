"""A function that checks whether a word is a palindrome or not

    Arguments:
        word {String} -- Word to be checked
        
    Raises:
        AssertionError: _description_

    Returns:
        Bool -- Whether passed string is a palindrome or not
"""

def isPalindrome(word):
    
    # IF PASSED ARGUMENT IS LENGTH <=1 
        # RETURN TRUE
    if len(word) <= 1:
        return True
    
    # IF FIRST AND LAST CHARACTERS ARE NOT EQUAL
        # USE STRING SLICING TO ACCESS LETTERS
        # RETURN FALSE
    # first = word[0]
    # last  = word[-1]
    # print(first)
    # print(last)
    if (word[0] != word[-1]):
        return False
        
    # DO A RECURSIVE CALL 
        # WE KNOW THAT THE FIRST AND LAST CHARACTERS OF THE WORD ARE THE SAME
        # PASS THE WORD TO THE FUNCTION WITHOUT THE FIRST AND LAST CHARACTERS
    # print (f"{word[1:-1]}")
    
    return isPalindrome(word[1:-1])


if __name__=="__main__":
    
    # Get input from user
    attempt = 0
    max_attempt = 3

    palindrome = False

    while palindrome == False:

        word_to_check = input(f"Enter a word to see if it is a palindrome. You have {max_attempt - attempt} attempts. :: ")

        attempt += 1
        
        if (len(word_to_check)) == 0:
            print ("The word can't be an empty string. 1 attempt used.  Try again.")
        else:
            
            palindrome = isPalindrome(word_to_check.upper())
            
            if attempt == max_attempt and palindrome == False:
                print (f"Reached maximum attempts of {max_attempt}.")
                break

    if palindrome == False:
        print (f"No palindromes were entered after {max_attempt} attempts.")
    else:
        print (f"'{word_to_check}' is a palindrome.")
