class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0

        for n in nums:
            tmp1, tmp2 = n + k, n - k
            counter += (seen[tmp1] + seen[tmp2])
            seen[n] += 1
        
        return counter
