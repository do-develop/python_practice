class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        N = len(nums)
        for x, y in queries:
            tmp = []
            for idx in range(N):
                trimmed = nums[idx][-y:]
                trimmed = int(trimmed)

                if len(tmp) < x:
                    heapq.heappush(tmp, [-1 * trimmed, -idx])
                else:
                    if trimmed < -tmp[0][0]:
                        heapq.heappop(tmp)
                        heapq.heappush(tmp, [-1 * trimmed, -idx])
            answer.append(-heapq.heappop(tmp)[1])
        return answer
