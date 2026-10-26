class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        states = defaultdict(int)
        curr_state, ans = (0, 0), 0
        states[curr_state] = -1

        for idx, num in enumerate(nums):
            xor_, state = curr_state
            curr_state = (xor_ ^ num, state + 2 * (num % 2) - 1)

            if curr_state not in states:
                states[curr_state] = idx
            else:
                span = idx - states[curr_state]
                if span > ans:
                    ans = span
        
        return ans