class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.count = 0
        paths = set()
        graph = collections.defaultdict(list)
        for start, end in connections:
            paths.add((start, end))
            graph[start].append(end)
            graph[end].append(start)

        def dfs(cur, parent):
            self.count += (parent, cur) in paths
            for neigh in graph[cur]:
                if neigh == parent:
                    continue
                dfs(neigh, cur)
        dfs(0, -1)
        return self.count
