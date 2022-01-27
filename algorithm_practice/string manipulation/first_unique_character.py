# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.
# Note: all the input strings are already lowercase.

#Approach 1
def first_unique_char(str):
    frequency = {}
    for i in str:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    for i in range(len(str)):
        if frequency[str[i]] == 1:
            return i
    return -1

print(first_unique_char('alphabet'))
print(first_unique_char('barbados'))
print(first_unique_char('crunchy'))

#Approach 2
import collections

def first_unique_letter(str):
    # build hash map of character and how often it appears
    count = collections.Counter(str)
    # <-- gives back a dictionary with words occurrence count
    # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})

    #find the index
    for idx, char in enumerate(str):
        if count[char] == 1:
            return idx
    return -1

print(first_unique_letter('aloha'))
print(first_unique_letter('barbados'))
print(first_unique_letter('crunchy'))
