class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        maxi, heap = 0,  []

        for bit, score in zip(s, nums):
            if bit == "1":
                maxi -= heappushpop(heap, -score)
            else:
                heappush(heap, -score)
        return maxi