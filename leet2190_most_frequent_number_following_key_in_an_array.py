class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = Counter()
        N = len(nums)

        for i, v in enumerate(nums):
            if v == key and i + 1 < N:
                counter[nums[i + 1]] += 1
        
        return counter.most_common(1)[0][0]
