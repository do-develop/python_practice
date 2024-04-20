class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        average = [-1] * N
        window_size = 2 * k  + 1

        if window_size > N:
            return average
        
        window_sum = 0
        for n in nums[:window_size]:
            window_sum += n
        
        average[k] = window_sum // window_size
        for i in range(k + 1, N - k):
            window_sum += nums[k + i] - nums[i - k - 1]
            average[i] = window_sum // window_size
        return average
