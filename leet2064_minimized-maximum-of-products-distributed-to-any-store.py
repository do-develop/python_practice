class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search problem
        # given mid restriction for each shop, how many shops we need to distribute all goods
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            total = 0
            for qnt in quantities:
                total += ceil(qnt / mid)
            if total > n:
                left = mid + 1
            else:
                right = mid
        return left
