class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if max(nums) == 0: return 0    
        ans = -1

        for idx, num in enumerate(nums):
            counts = {num} # set of all values reachable at this index

            for pos, (left, right, val) in enumerate(queries):
                if left <= idx <= right:
                    shift = {x - val for x in counts if x >= val}
                    counts |= shift # union back into counts

                if 0 in counts:
                    # keep track of the latest index to be resolved
                    ans = max(ans, pos + 1)
                    break
            
            if 0 not in counts:
                return -1

        return ans
