class Solution:
    def minSteps(self, s: str, t: str) -> int:
        source = Counter(list(s))
        target = Counter(list(t))
        intersect_sum = 0

        for char, val in source.items():
            if char in target:
                intersect_sum += min(val, target[char])

        return len(s) + len(t) - (2 * intersect_sum)        
