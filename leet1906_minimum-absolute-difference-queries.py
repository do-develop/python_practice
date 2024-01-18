class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # cumulative sum approach
        maxnum = max(nums)
        N = len(nums)
        presum = [[0] * (maxnum + 1)] # cumulative counters of numbers

        for num in nums:
            cursum = presum[-1][:]
            cursum[num] += 1
            presum.append(cursum)
        
        ans = []

        for l, r in queries:
            mmin = sys.maxsize
            pre = -1
            for num in range(1, maxnum + 1):
                # check difference between windows
                diff = presum[r + 1][num] - presum[l][num]
                if diff > 0: # num under this condition needs to be checked
                    if pre != -1:
                        mmin = min(mmin, num - pre)
                    pre = num
            ans.append(mmin if mmin < sys.maxsize else -1)
        return ans
