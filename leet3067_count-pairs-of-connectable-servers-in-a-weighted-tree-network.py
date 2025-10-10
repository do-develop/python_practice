class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, weight in edges:
            graph[x].append([y, weight])
            graph[y].append([x, weight])
        
        result = [0] * (len(edges) + 1)
        for server in range(len(edges) + 1):
            total_pairs = 0
            subtree_counts = []

            for neigh, edge_weight in graph[server]:
                count = [0]
                self.dfs(neigh,server, graph, edge_weight, count, signalSpeed)
                subtree_counts.append(count[0])

            for i in range(len(subtree_counts)):
                for j in range(i + 1, len(subtree_counts)):
                    total_pairs += subtree_counts[i] * subtree_counts[j]

            result[server] = total_pairs
        return result
    
    def dfs(self, curr_node, parent_node, graph, curr_weight, count, signal_speed):
        if curr_weight % signal_speed == 0:
            count[0] += 1
        for neighbor, edge_weight in graph[curr_node]:
            if neighbor == parent_node:
                continue
            self.dfs(neighbor, curr_node, graph, curr_weight + edge_weight, count, signal_speed)
