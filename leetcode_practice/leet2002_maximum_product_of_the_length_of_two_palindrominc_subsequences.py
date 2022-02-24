"""
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.
"""
# bit mask approach

class Solution:
    def maxProduct(self, s: str) -> int:
        N, palind = len(s), {} # bitmask : length

        for mask in range(1, 1 << N): # 1 << N == 2 ** N
            subseq = ""
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                palind[mask] = len(subseq)
                
        result = 0
        for m1 in palind:
            for m2 in palind:
                if m1 & m2 == 0: #disjoint
                    result = max(result, palind[m1] * palind[m2])
        return result
        
        


s = "leetcodecom"
print(Solution().maxProduct(s))
"""
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence
and "cdc" for the 2nd subsequence. The product of their lengths is: 3 * 3 = 9.
"""
