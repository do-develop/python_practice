class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for elem in arr:
            freq[elem] = freq[elem] + 1
        
        q = []
        for v in freq.values():
            neg_v = -v
            heapq.heappush(q, neg_v)
        
        remove_count = total = 0
        half = len(arr) / 2

        while total < half:
            remove_count += 1
            total += (-heapq.heappop(q))
        
        return remove_count
