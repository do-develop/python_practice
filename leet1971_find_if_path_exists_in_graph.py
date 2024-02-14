class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for edge in edges:
            src, des = edge
            graph[src].append(des)
            graph[des].append(src)
        
        visited = set()
        def has_path(node):
            if node == destination:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    if has_path(neigh):
                       return True
            return False

        return has_path(source) 
