class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [None] * len(graph)
        for i in range(len(graph)):
            if colors[i] is None:
                colors[i] = 1
                queue = [i]
                while queue:
                    cur = queue.pop(0)
                    for node in graph[cur]:
                        if colors[node] is None:
                            colors[node] = 1 - colors[cur]
                            queue.append(node)
                        elif colors[node] == colors[cur]:
                            return False
        return True
        
