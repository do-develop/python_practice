"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C',
'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence. When studying DNA, it is useful to
identify repeated sequences within the DNA. Given a string s that represents a
DNA sequence, return all the 10-letter-long sequences (substrings) that occur
more than once in a DNA molecule. You may return the answer in any order.
"""
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()

        for l in range(len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                repeated.add(cur)
            seen.add(cur)
        return list(repeated)


# TEST
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))
#Output: ["AAAAACCCCC","CCCCCAAAAA"]
