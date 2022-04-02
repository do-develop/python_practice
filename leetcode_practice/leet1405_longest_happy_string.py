"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
"""
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            # most common char
            count, char = heapq.heappop(maxHeap)
            # can't add 3 consequent char
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                result += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                result += char
                count += 1
            # char still left, put it back in
            if count :
                heapq.heappush(maxHeap, (count, char))
                
        return result




# TEST
a = 1
b = 1
c = 7
print(Solution().longestDiverseString(a,b,c))
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
