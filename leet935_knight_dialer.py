class Solution:
    def knightDialer(self, n: int) -> int:
        # dp approach
        # dictionary of possible next number (destination)
        dest = {
            0: (4, 6),
            1: (6, 8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        }
        NUM_KEY = 10
        dp = [1] * NUM_KEY # start from 1 jump
        # n - 1 = count of jumps
        for _ in range(n - 1):
            nxt = [0] * NUM_KEY
            for i in dest:
                for j in dest[i]:
                    nxt[j] += dp[i]
            dp = nxt # update dp
        return sum(dp) % (10 ** 9 + 7)
