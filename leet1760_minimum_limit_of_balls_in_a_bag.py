class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # approch - binary search the size
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2 # mid is the size to divide the num
            # if the total operation needed for the size (mid) is samller than the max ops
            if sum((n - 1) // mid for n in nums) > maxOperations:
                left = mid + 1  # increase the size
            else:
                right = mid     # decrease the size
        return left
