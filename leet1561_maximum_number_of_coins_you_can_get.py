class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_idx = len(piles) - 1
        ans = 0
        for i in range(len(piles) // 3):
            max_idx -= 1 # Alice
            ans += piles[max_idx]
            max_idx -= 1 # I just picked
        return ans
