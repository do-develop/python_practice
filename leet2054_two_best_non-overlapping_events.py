class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # sort by start date, track end time in min heap
        # remove past event from the min heap, track the max value so far
        ans = cur_max = 0
        q = []
        for s, e, v in sorted(events):
            while q and q[0][0] < s:
                cur_max = max(cur_max, heappop(q)[1])
            ans = max(ans, cur_max + v)
            heappush(q, (e, v))
        return ans
