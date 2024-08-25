class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest = 0

        for i in range(24):
            total = 0
            for c in candidates:
                total += (c >> i) & 1
            largest = max(largest, total)
        return largest
