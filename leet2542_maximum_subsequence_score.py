class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = score = 0
        heap = []
        for n1, n2 in sorted(list(zip(nums1, nums2)), key=lambda x:-x[1]):
            heappush(heap, n1)
            total += n1
            
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                score = max(score, total * n2)
        return score
