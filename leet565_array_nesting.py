class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        longest = 0

        for n in nums:
            cnt = 0
            while not visited[n]:
                cnt += 1
                visited[n] = True
                n = nums[n]
            longest = max(longest, cnt)
        
        return longest
