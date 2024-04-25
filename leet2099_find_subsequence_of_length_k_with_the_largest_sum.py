class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # priority queue(HEAP) approach
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap) # smallest is popped

        # now need to get the order right
        counter = Counter(heap)
        subseq = []
        for n in nums:
            if counter[n] > 0:
                counter[n] -= 1
                subseq.append(n)
        return subseq
