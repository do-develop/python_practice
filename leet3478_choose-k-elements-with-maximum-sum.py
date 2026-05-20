class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        N = len(nums1)
        answer = [0] * N

        indices = sorted(range(N), key=lambda i: nums1[i])
        min_heap = []
        heap_sum = 0

        i = 0
        while i < N:
            j = i
            while j < N and nums1[indices[j]] == nums1[indices[i]]:
                j += 1
            
            for idx in indices[i:j]:
                answer[idx] = heap_sum

            for idx in indices[i:j]:
                heapq.heappush(min_heap, nums2[idx])
                heap_sum += nums2[idx]
                if len(min_heap) > k:
                    heap_sum -= heapq.heappop(min_heap)
        
            i = j

        return answer
