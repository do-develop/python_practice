"""
Alice has some number of cards and she wants to rearrange the cards into groups
so that each group is of size groupSize, and consists of groupSize consecutive
cards. Given an integer array hand where hand[i] is the value written on the
ith card and an integer groupSize, return true if she can rearrange the cards,
or false otherwise.
"""
from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    heapq.heappop(min_heap)
                    
        return True
        




# TEST
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(Solution().isNStraightHand(hand, groupSize))
# expected output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
