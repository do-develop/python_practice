class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        s = list(s)
        balance = swaps = 0
        r = N - 1
        for l in range(N):
            if s[l] == '[':
                balance += 1
            else:
                balance -= 1
        
            if balance < 0:
                while l < r and s[r] != '[':
                    r -= 1
                s[l], s[r] = s[r], s[l]
                swaps += 1
                balance = 1
        return swaps
