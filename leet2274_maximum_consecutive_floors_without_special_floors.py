class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        res = max(top - special[-1], special[0] - bottom)
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i - 1] - 1)
        return res
