class Solution:
    def minimumDeletions(self, s: str) -> int:
        # At every point in our traversal, if encounter an "a", 
        # delete every "b" up to that point, or delete that one "a"
        result = 0
        b_count = 0
        for c in s:
            if c == 'a':
                result = min(b_count, result + 1)
            else:
                b_count += 1
        return result
