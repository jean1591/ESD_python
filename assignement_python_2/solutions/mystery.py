from pprint import pprint
from string import ascii_uppercase

def some_function(some_string):
    """Display keyboard with letters from some_string

    Args:
        some_string (string): String from which to extract letters

    Returns:
        list: 2D list representing keyboard
    """
    
    # Init empty list and 2D list
    letters = []
    res = [[" "] * 10, [" "] * 10, [" "] * 10]

    # Loop uppercase letters from some_string
    for letter in some_string.upper():
        # Check if letter in ascii_uppercase and if letter is not already in letters list
        if letter in ascii_uppercase and letter not in letters:
            # Add letter to letters list
            letters.append(letter)
            
            row = -1
            col = -1
            
            # Check if letter is i n first row of keyboard
            if letter in "AZERTYUIOP":
                # Update row to 0 and col to location of letter within "AZERTYUIOP"
                row = 0
                col = "AZERTYUIOP".index(letter)
            elif letter in "QSDFGHJKLM":
                row = 1
                col = "QSDFGHJKLM".index(letter)
            elif letter in "WXCVBN":
                row = 2
                col = "WXCVBN".index(letter)
            
            # Check if row & col have been updated
            if row != -1 and col != -1:
                # Update 2D list (res) 
                res[row][col] = letter

    # Return 2D list (res)
    return res


pprint(some_function("some_string"))
print()
pprint(some_function("jean"))
print()
pprint(some_function("esd"))
print()
pprint(some_function("hello world"))