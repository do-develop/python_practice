class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        
        diffs.sort() # sort by difference
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2: # first half
                res += diffs[i][2]
            else:                   # second half
                res += diffs[i][1]
        return res
