class Solution:
    def maxProduct(self, s: str) -> int:
        # bit mask & operation (both needs to be 1 to get 1)
        # can be used if the subsequences are disjoint
        N, pali = len(s), {} # bitmask -> length

        for mask in range(1, 1 << N): # 2 ** N
            subseq = ''
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)
        
        max_len = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    max_len= max(max_len, pali[m1] * pali[m2])
        return max_len
