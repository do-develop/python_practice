class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # sort then find max rectangle
        max_rect, N = 0, len(beans)
        for i, bean in enumerate(sorted(beans)):
            max_rect = max(max_rect, (N - i) * bean)
        return sum(beans) - max_rect
