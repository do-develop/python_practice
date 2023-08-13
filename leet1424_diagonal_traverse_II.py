class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        q = collections.deque([(0,0)])
        while q:
            r, c = q.popleft()
            ans.append(nums[r][c])
            if c == 0 and r + 1 < len(nums):
                q.append((r + 1, c))
            if c + 1 < len(nums[r]):
                q.append((r, c + 1))
        return ans
