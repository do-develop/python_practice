"""
Given a string paragraph and a string array of the banned words banned,
return the most frequent word that is not banned. It is guaranteed there
is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.
"""
from typing import List
import collections
import re

class Solution:
    def most_common_word(self, paragraph: str, banned: List[str]) -> str:
        # pre-process to cleanse the data
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split() if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it hit."
banned = ["hit"]
print(Solution.most_common_word(Solution, paragraph, banned))