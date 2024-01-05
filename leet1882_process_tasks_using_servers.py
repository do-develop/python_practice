class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # two heaps approach
        ans, unavailable, time = [], [], 0
        available = [(weight, idx) for idx, weight in enumerate(servers)]
        heapify(available) # sort by smallest weight

        for task in tasks:
            while unavailable and unavailable[0][0] == time:
                _, weight, idx = heappop(unavailable)
                heappush(available, (weight, idx))

            if len(available) > 0 :
                weight, idx = heappop(available)
                heappush(unavailable, (time + task, weight, idx))
                ans.append(idx)
            else: # to reduce time just queue up the next task instaed of waiting for time to pass
                finish_time, weight, idx = heappop(unavailable)
                heappush(unavailable, (finish_time + task, weight, idx))
                ans.append(idx)
            time += 1
        return ans
