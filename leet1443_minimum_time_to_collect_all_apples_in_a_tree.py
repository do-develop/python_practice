class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # construct tree(undirected graph) using the edges
        tree = defaultdict(list)
        for start, end in  edges:
            tree[start].append(end)
            tree[end].append(start)

        def dfs(node, parent):
            path = 0
            # visit neighbors of the current node
            for nei in tree[node]:
                if nei != parent: # make sure we don't go back to parent
                    path += dfs(nei, node)
            # path != 0 means there is apple on this path
            # or there is apple on this node, either way it takes two time units
            if path or hasApple[node]:
                path += 2 if node != 0 else 0
                return path
            # if no apple on this path, then return 0
            return path

        return dfs(0, -1)
