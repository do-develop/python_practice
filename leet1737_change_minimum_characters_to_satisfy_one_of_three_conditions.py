class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        count1 = Counter(ord(c) - 97 for c in a)
        count2 = Counter(ord(c) - 97 for c in b)
        res = len_a + len_b - max((count1 + count2).values()) # condition 3

        for c in range(25):
            count1[c + 1] += count1[c]
            count2[c + 1] += count2[c]
            res = min(res, len_a - count1[c] + count2[c]) # condition 1
            res = min(res, len_b - count2[c] + count1[c]) # condition 2
        return res
