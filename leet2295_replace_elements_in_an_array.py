class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        positions = defaultdict(int)
        N = len(nums)
        for i in range(N):
            positions[nums[i]] = i

        for op in operations:
            nums[positions[op[0]]] = op[1]
            # update new position
            positions[op[1]] = positions[op[0]]
        return nums
