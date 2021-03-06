"""
Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any
order. Each task is done in one unit of time. For each unit of time, the
CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown
period between two same tasks (the same letter in the array), that is that
there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish
all the given tasks.
"""
from collections import Counter, deque
from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        # to make it max heap put negative value
        left_count = [-cnt for cnt in count.values()]
        heapq.heapify(left_count)

        time = 0
        q = deque()  # pairs of [-cnt, idle_time]

        while left_count or q:
            time += 1

            if left_count:
                cnt = 1 + heapq.heappop(left_count)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(left_count, q.popleft()[0])
        return time

# Test
tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))