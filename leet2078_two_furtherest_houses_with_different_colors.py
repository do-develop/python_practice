class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Greedy approach - Find either:
        # the last house with diff color from the first house
        # the first house with diff color from the last house
        N = len(colors)
        left, right = 0, N - 1
        while colors[0] == colors[right]: right -= 1
        while colors[-1] == colors[left]: left += 1
        return max(right, N - 1 - left)
