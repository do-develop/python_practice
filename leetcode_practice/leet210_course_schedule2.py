"""
There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i]
= [ai, bi] indicates that you must take course bi first if you want to take
course ai. Return the ordering of courses you should take to finish all
courses. If there are many valid answers, return any of them. If it is
impossible to finish all courses, return an empty array.
"""
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list
        prereq = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # topology sort
        output = []
        visited, cycle = set(), set()

        def dfs(crs):
            # base case
            if crs in cycle:
                return False
            if crs in visited:
                return True

            # check for sign of cycle
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            # no sign of cycle
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)

        # perform topology sort
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        
                

# TEST
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))
# Expected Output: [0,2,1,3]
