class Solution:
    def lexSmallest(self, s: str) -> str:
        N = len(s)
        ans = s

        for k in range(1, N + 1):
            case1 = s[:k][::-1] + s[k:]
            ans = min(ans, case1)
            case2 = s[:N-k] + s[N-k:][::-1]
            ans = min(ans, case2)
        
        return ans