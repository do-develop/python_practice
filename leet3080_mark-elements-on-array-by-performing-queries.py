class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        marked = set()
        ans = []

        heap = [(value, i) for i, value in enumerate(nums)]
        heapify(heap)
        total = sum(nums)

        for idx, k in queries:
            if idx not in marked:
                marked.add(idx)
                total -= nums[idx]
            
            while k > 0 and heap:
                val, i = heappop(heap)
                if i not in marked:
                    marked.add(i)
                    total -= val
                    k -= 1
            ans.append(total)
        return ans
