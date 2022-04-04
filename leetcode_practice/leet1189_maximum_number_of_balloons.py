"""
Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible. You can use each character in
text at most once. Return the maximum number of instances that can be formed.
"""
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        result = float("inf")
        for c in balloon:
            result = min(result, countText[c] // balloon[c])
        return result



# TEST
text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))
# Output: 2
