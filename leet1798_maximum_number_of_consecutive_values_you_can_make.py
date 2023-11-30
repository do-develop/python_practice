class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res = 1 # next target value
        for coin in coins:
            # all remaining number is bigger than res
            if coin > res:
                break
            # can make from 0 to res - 1
            res += coin
        return res
