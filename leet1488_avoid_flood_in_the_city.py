class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        rain_day = collections.defaultdict(list)
        full = set([])
        urgent = []

        for day, lake in enumerate(rains):
            rain_day[lake].append(day)

        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                rain_day[lake].pop(0)
                if rain_day[lake]:
                    heapq.heappush(urgent, rain_day[lake][0])
            else:
                if urgent:
                    ans[i] = rains[heapq.heappop(urgent)]
                    full.remove(ans[i])
                else:
                    ans[i] = 1
        return ans
