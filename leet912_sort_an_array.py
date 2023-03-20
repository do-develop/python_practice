class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    # merge sort approach
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[:mid]
                right = nums[mid:]
                merge_sort(left)
                merge_sort(right)
                l = r = k = 0
                while l < len(left) and r < len(right):
                    if left[l] < right[r]:
                        nums[k] = left[l]
                        l += 1
                    else:
                        nums[k] = right[r]
                        r += 1
                    k += 1
                while l < len(left):
                    nums[k] = left[l]
                    l += 1
                    k += 1
                while r < len(right):
                    nums[k] = right[r]
                    r += 1
                    k += 1
        merge_sort(nums)
        return  nums
