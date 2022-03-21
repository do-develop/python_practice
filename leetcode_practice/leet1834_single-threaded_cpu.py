"""
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array
tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task
will be available to process at enqueueTimei and will take processingTimei to
finish processing.

You have a single-threaded CPU that can process at most one task at a time and
will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains
idle. If the CPU is idle and there are available tasks, the CPU will choose the
one with the shortest processing time. If multiple tasks have the same shortest
processing time, it will choose the task with the smallest index. Once a task is
started, the CPU will process the entire task without stopping. The CPU can
finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.
"""
from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add indices as we need original order for the answer
        for idx, task in enumerate(tasks):
            task.append(idx)
            
        # sort by enqueue time
        tasks.sort(key = lambda t: t[0])

        #declare variables before processing
        result, min_heap = [], []
        i, time = 0, tasks[0][0]  # tasks index, smallest enqueue time

        while i < len(tasks) or min_heap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not min_heap:
                time = tasks[i][0]
            else:
                proc_time, index = heapq.heappop(min_heap)
                time += proc_time
                result.append(index)

        return result
                
        




# TEST
tasks = [[1,2],[2,4],[3,2],[4,1]]
print(Solution().getOrder(tasks))
# expected output: [0,2,3,1]
