# Method 1 - Two pointer to swap
from typing import List
"""
def reverse_string(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
"""

# Method 2 - reverse() function
def reverse_string(s: List[str]) -> None:
    s.reverse()

hello = ["h", "e", "l", "l", "o"]
reverse_string(hello)
print(hello)
