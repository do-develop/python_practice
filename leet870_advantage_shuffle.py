class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sorte in descending order
        nums2 = sorted([(num, i) for i, num in enumerate(nums2)])[::-1]
        nums1 = sorted(nums1)[::-1]
        ans = [-1] * len(nums1)

        # two pointers
        beg, end = 0, len(nums1)-1

        for num, idx in nums2:
            if nums1[beg] > num:
                ans[idx] = nums1[beg]
                beg += 1
            else:
                ans[idx] = nums1[end]
                end -= 1
        return ans
