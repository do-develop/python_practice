# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.


str = 'madam'

def checkPalindrome(str):
    for i in range(len(str)):
        t = str[:i] + str[i+1:]
        if t == t[::-1]: return True
    return str == str[::-1]

if(checkPalindrome(str)):
    print("It is palindrome!")
else:
    print("It is not a palindrome")