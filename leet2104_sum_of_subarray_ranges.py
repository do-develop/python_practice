class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # brute-force approach (2 loops)
        '''
        answer = 0
        N = len(nums)
        for left in range(N):
            minVal, maxVal = math.inf, -math.inf
            for right in range(left, N):
                minVal = min(minVal, nums[right])
                maxVal = max(maxVal, nums[right])
                answer += maxVal - minVal
        return answer
        '''
        # O(n) solutipn using monotonic stack
        answer = 0
        N = len(nums)
        stack = []

        # - the sum of minimums
        for right in range(N + 1):
            while stack and (right == N or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # the sum of  maximums
        stack.clear()
        for right in range(N + 1):
            while stack and (right == N or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        return answer
