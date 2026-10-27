MOD = 10**9 + 7
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        sum = [0] * (N + 1)
        x = [0] * (N + 1)
        count = [0] * (N + 1)

        for i, c in enumerate(s):
            digit = int(c)
            sum[i + 1] = sum[i] + digit
            x[i + 1] = (x[i] * 10  + digit) % MOD if digit > 0 else x[i]
            count[i + 1] = count[i] + (digit > 0)

        M = len(queries)
        res = [0] * M
        for i in range(M):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = count[r] - count[l]
            res[i] = (x[r] - x[l] * pow10[length]) * (sum[r] - sum[l]) % MOD
        
        return res
