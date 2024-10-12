class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        counter = defaultdict(int)

        for i in range(N):
            nums[i] -= i
            counter[nums[i]] += 1

        goodCnt = 0
        for key in counter:
            goodCnt += math.comb(counter[key], 2)
            
        return math.comb(N, 2) - goodCnt
