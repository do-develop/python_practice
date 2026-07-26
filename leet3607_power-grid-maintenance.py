class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(c + 1)]
        for u, v in connections:
            adjacency[u].append(v)
            adjacency[v].append(u)
        
        # component_root[i] = smallest node index in i's connected component
        component_root = [0] * (c + 1)

        def flood_fill(node, root_label):
            if component_root[node]: return
            component_root[node] = root_label
            for neigh in adjacency[node]:
                flood_fill(neigh, root_label)
            return
        
        for node in range(1, c + 1):
            flood_fill(node, node)
        
        component_nodes = defaultdict(list)
        for node in range(c, 0, -1):
            component_nodes[component_root[node]].append(node)

        is_online = [1] * (c + 1)
        res = []

        for query_type, x in queries:
            if query_type == 1:
                if is_online[x]:
                    res.append(x)
                    continue
                root = component_root[x]
                candidates = component_nodes[root]
                # discard offline nodes
                while candidates and not is_online[candidates[-1]]:
                    candidates.pop()
                res.append(candidates[-1] if candidates else -1)
            elif query_type == 2:
                is_online[x] = 0
        
        return res