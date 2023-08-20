class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # topological sort
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses
        pres = [set() for _ in range(numCourses)]
        for pre, crs in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1
            pres[crs].add(pre)
        
        q = collections.deque(crs for crs, degree in enumerate(in_degree) if degree == 0)
        while q:
            pre = q.popleft()
            for crs in graph[pre]:
                pres[crs] |= pres[pre]  # union between two sets
                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    q.append(crs)
        return [pre in pres[crs] for pre, crs in queries]
