"""
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.
"""
from typing import List
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        path = set()
        visited_node = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited_node:
                return True

            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            path.remove(course)
            visited_node.add(course)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

# Driver code
numCourses = 5
prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(Solution().canFinish(numCourses, prerequisites))