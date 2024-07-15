class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Binary search approach to find the maximum candies
        left, right = 0, sum(candies) // k

        while left < right:
            # add 1 to (l + r) to ensure that mid - 1 gets the correct middle index
            mid = (left + right + 1) // 2
            if k > sum(pile // mid for pile in candies):
                right = mid - 1
            else:
                left = mid
        return left
