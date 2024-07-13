class Solution:
    def numberOfWays(self, s: str) -> int:
        # There are only 2 valid patterns: ‘101’ and ‘010’
        ones, zeros, ways = 0, 0, 0
        N = len(s)

        # Count ones and zeros
        for i in range(N):
            if s[i] == '1':
                ones += 1
            else:
                zeros += 1
        
        prev_ones, prev_zeros = 0, 0
        for i in range(N):
            if s[i] == '1':
                ways += prev_zeros * zeros
                ones -= 1
                prev_ones += 1
            else:
                ways += prev_ones * ones
                zeros -= 1
                prev_zeros += 1
        return ways
