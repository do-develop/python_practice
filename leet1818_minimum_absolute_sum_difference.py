class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # sort num1 and perform binary search to find idx
        # find min_diff = abs(sorted1[idx] - nums2[i]) or abs(sorted1[idx - 1] - nums2[i])
        # and find the max difference mx = diff - min_diff
        diff_sum, mx = 0, -math.inf
        sorted1 = sorted(nums1)
        for i, (n1, n2) in enumerate(zip(nums1, nums2)):
            # save the difference sum
            diff = abs(n1 - n2)
            diff_sum += diff
            # find the max difference that can be made by replacing 1 number in nums1
            idx = bisect.bisect_left(sorted1, n2)
            if idx < len(sorted1):
                mx = max(mx, diff - abs(sorted1[idx] - n2))
            if idx > 0:
                mx = max(mx, diff - abs(sorted1[idx - 1] - n2))
        return (diff_sum - mx) % (10 ** 9 + 7)
