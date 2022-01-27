"""
# Method 1 - List
def is_palindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): #consider only alphabet and number
            strs.append(char.lower()) #does not need to check case
    #check palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

"""

"""
import collections

# Method 2 - Deque
def is_palindrome(s: str) -> bool:
    # Deque is preferred over list in the cases where we need quicker append and pop operations
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
"""

# Method 3 - Slicing
import re

def is_palindrome(s: str) -> bool:
    s = s.lower()
    # use regex to filter unwanted characters
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]

str = 'A man, a plan, a canal: Panama'

if is_palindrome(str):
    print("It is palindrome!")
else:
    print("It is not a palindrome")