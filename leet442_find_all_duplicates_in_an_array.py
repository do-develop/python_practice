class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(1) space complexity solution
        duplicates = []
        for n in nums:
            if nums[abs(n) - 1] < 0:    # if the element at the index negative, it is already seen (found duplicate)
                duplicates.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1  # mark the element at the index negative
        return duplicates
