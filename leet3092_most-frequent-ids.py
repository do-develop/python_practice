class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        counter = defaultdict(int)
        N = len(nums)
        heap = []
        res = [0] * N

        for i, (num, cnt) in enumerate(zip(nums, freq)):
            counter[num] += cnt
            heappush(heap, [-counter[num], num])
            #  check removal condition
            while heap and -heap[0][0] != counter[heap[0][1]]:
                heappop(heap)
            if heap:
                res[i] = -heap[0][0]
        return res

