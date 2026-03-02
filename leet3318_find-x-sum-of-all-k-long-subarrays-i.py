class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        ans = list()

        for i in range(N - k + 1):
            count = Counter(nums[i: i + k])
            freq = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
        return ans
