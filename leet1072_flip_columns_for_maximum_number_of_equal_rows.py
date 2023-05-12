class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # the problem comes down to finding the max number of
        # rows that has the same pattern or opposite pattern
        patterns = collections.Counter()
        for row in matrix:
            patterns[tuple(row)] += 1
            flip = [1 - n for n in row]
            patterns[tuple(flip)] += 1
        return max(patterns.values())
