from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for idx, val in enumerate(t):
                if val == target[idx]:
                    good.add(idx)

        return len(good) == 3




triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print(Solution().mergeTriplets(triplets, target))
# Output: true
"""
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]].
Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5].
triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.
"""
