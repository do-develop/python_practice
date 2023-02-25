class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minheap = list(count.keys())
        heapq.heapify(minheap)
        while minheap:
            first = minheap[0] # start from the min value

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minheap[0]: # the value to be popped is not min value
                        return False
                    heapq.heappop(minheap)
        return True
