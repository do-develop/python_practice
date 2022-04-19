"""
Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same. Return any possible rearrangement of s or
return "" if not possible.
"""
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        result = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            # most frequest, except prev
            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
                
            if cnt != 0:
                prev = [cnt, char]
        return result

# TEST
s = "aab"
print(Solution().reorganizeString(s))
#Output: "aba"
