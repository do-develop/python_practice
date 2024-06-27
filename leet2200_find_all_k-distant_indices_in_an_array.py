class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        positions = []

        for idx, val in enumerate(nums):
            if val == key:
                positions.append(idx)
            
        res = []
        for i in range(len(nums)):
            for pos in positions:
                if abs(i -pos) <= k:
                    res.append(i)
                    break
        return sorted(res)
