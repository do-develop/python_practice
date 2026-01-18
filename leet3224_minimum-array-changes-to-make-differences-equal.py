class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        N = len(nums)
        change_range = [0 for _ in range(k + 2)]

        # Difference array marks the boundaries where number of changes increases or decreases
        for i in range(N // 2):
            left, right = nums[i], nums[N - i - 1]
            cur_diff, max_diff = abs(right - left), max(left, right, k -left, k - right)
            change_range[0] += 1
            change_range[cur_diff] -= 1
            change_range[cur_diff + 1] += 1
            change_range[max_diff + 1] += 1

        # Prefix sum
        cur_change, min_change = 0, N
        for i in range(k + 1):
            cur_change += change_range[i]
            min_change = min(min_change, cur_change)
        return min_change
