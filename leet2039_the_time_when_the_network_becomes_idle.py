class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # BFS approach to get the shortest path from node to master
        # calculate last resent time, how long will it take to reach the server after that
        adjency = defaultdict(list)

        for s, d in edges:
            adjency[s].append(d)
            adjency[d].append(s)
        
        shortest = {}
        q = deque([(0,0)])
        seen = set()

        # BFS to find shortest route to master server
        while q:
            pos, dist = q.popleft()
            if pos in seen:
                continue
            seen.add(pos)
            shortest[pos] = dist

            for nei in adjency[pos]:
                q.append((nei, dist + 1))
            
        ans = 0
        for idx in range(1, len(patience)):
            interval = patience[idx]
            # sent to the master node and back
            shutoff_time = shortest[idx] * 2
            # the time that the server can send a re-request.
            last_second = shutoff_time - 1
            # last time a packet is actually sent
            last_resent_time = (last_second // interval) * interval
            last_packet_time = last_resent_time + shutoff_time

            ans = max(last_packet_time, ans)
        return ans + 1 # the first second that the network is idle = the last packet arrival time + 1
