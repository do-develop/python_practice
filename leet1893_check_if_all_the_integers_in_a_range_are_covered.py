class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start, end in ranges:
            if end < left: continue
            if start > left: return False
            left = max(left + 1, end + 1)
            if left - 1 >= right:
                return True
        return False
