class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        counts = collections.defaultdict(int)
        vl = sorted(zip(values, labels))
        ans = 0
        while numWanted and vl:
            val, lab = vl.pop()
            if counts[lab] < useLimit:
                ans += val
                counts[lab] += 1
                numWanted -= 1
        return ans
