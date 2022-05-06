"""
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of
limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""
# greedy algorithm
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        result = 0 # boats
        l, r = 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            result += 1
            if l <= r and remain >= people[l]:
                l += 1

        return result
        


people = [3,2,2,1]
limit = 3
print(Solution().numRescueBoats(people, limit))
#Output: 3
#Explanation: 3 boats (1, 2), (2) and (3)
