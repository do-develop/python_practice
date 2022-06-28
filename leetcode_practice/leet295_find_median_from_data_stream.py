"""
The median is the middle value in an ordered integer list. If the size of
the list is even, there is no middle value and the median is the mean of
the two middle values.
"""
import heapq

class MedianFinder:

    def __init__(self):
        # two heaps, a maxheap(small) and a minheap(large)
        self.small, self.large = [],[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # make sure every num small is <= every num in large
        if (self.small and self.large and
            (-1 * self.small[0]) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large) * -1
            heapq.heappush(self.small, val)
            
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((self.small[0] * -1) + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(3)
obj.addNum(1)
obj.addNum(2)
obj.addNum(7)
obj.addNum(8)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
