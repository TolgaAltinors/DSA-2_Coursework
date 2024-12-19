"""A function that checks whether a word is a palindrome or not

    Arguments:
        word {String} -- Word to be checked
        
    Raises:
        AssertionError: _description_

    Returns:
        Bool -- Whether passed string is a palindrome or not
"""

def isPalindrome(word):
    
    # IF PASSED ARGUMENT IS LENGTH 1 
        # RETURN TRUE
    if len(word) == 1:
        return True
    
    # IF FIRST AND LAST CHARACTERS ARE NOT EQUAL
        # USE STRING SLICING TO ACCESS LETTERS
        # RETURN FALSE
    first = word[0]
    last  = word[-1]
    print(first)
    print(last)
        
    # DO A RECURSIVE CALL 
        # PASS THE WORD TO THE FUNCTION WITHOUT THE FIRST AND LAST CHARACTERS
    return False


# Get input from user
attempt = 0
max_attempt = 5

palindrome = False

while palindrome == False:

    word_to_check = input("Enter a word to see if it is a palindrome. You have 5 attempts. :: ")

    attempt += 1
    
    if (len(word_to_check)) == 0:
        print ("The word can't be an empty string. 1 attempt used.  Try again.")
    else:
        
        palindrome = isPalindrome(word_to_check)
        
        if attempt == max_attempt and palindrome == False:
            print (f"Reached maximim attempt of {max_attempt}. Exiting")
            break

if palindrome == False:
    print (f"No palindrome were enetered after {max_attempt} attempts.")
else:
    print (f"'{word_to_check}' ia a palindrome")


