class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        str_set = {s for s in nums}
        N = len(nums)

        def backtrack(idx, cur):
            if idx == N:
                res = "".join(cur)
                return None if res in str_set else res
            
            # first decision (default 0)
            res = backtrack(idx + 1, cur)
            if res: return res

            # second decision (1)
            cur[idx] = "1"
            res = backtrack(idx + 1, cur)
            if res: return res

        return backtrack(0, ["0" for s in nums])
