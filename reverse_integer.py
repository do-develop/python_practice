# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1]) # -1 means backwards

# print the solution
print(reverse(-12345))
print(reverse(98765))
