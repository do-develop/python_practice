class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        rem = [[],[],[]]

        for n in nums:
            rem[n%3].append(n)
        
        maxi = 0
        if len(rem[0]) > 2:
            maxi = sum(rem[0][:3])
        if rem[0] and rem[1] and rem[2]:
            maxi = max(maxi, rem[0][0] + rem[1][0] + rem[2][0])
        if len(rem[1]) > 2:
            maxi = max(maxi, sum(rem[1][:3]))
        if len(rem[2]) > 2:
            maxi = max(maxi, sum(rem[2][:3]))
        return maxi