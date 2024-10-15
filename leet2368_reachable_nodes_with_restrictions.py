class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # BFS APPROACH
        # Restricted nodes are considered 'visited'
        neighbors = defaultdict(list)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        q = deque()
        q.append(0)
        result = 0
        visited = set()

        for node in restricted:
            visited.add(node)
        
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            result += 1
            for neigh in neighbors[curr]:
                q.append(neigh)
        return result
