class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # sliding window approach
        N = len(answerKey)

        def max_window(c):
            ans = flip = l = 0

            for r in range(N):
                if answerKey[r] != c:
                    flip += 1
                if flip > k:
                    while answerKey[l] == c:
                        l += 1
                    l += 1
                    flip -= 1 # decrement flip as the window adjusted
                ans = max(ans, r - l + 1)
            return ans
        return max(max_window('T'), max_window('F'))
