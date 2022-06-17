"""
Write a function that reverses a string. The input string is given as an array
of characters s. You must do this by modifying the input array in-place with
O(1) extra memory.
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        
        

s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)
# Output: ["o","l","l","e","h"]
