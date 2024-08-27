class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Greedy Approach: Place the additional rocks into 
        # the bag that need the least number of rocks
        missing = []
        full_bags = 0

        for idx, cap in enumerate(capacity):
            heapq.heappush(missing, cap - rocks[idx])
        
        while missing:
            additionalRocks -= heapq.heappop(missing)
            if additionalRocks >= 0:
                full_bags += 1
            else:
                break
        return full_bags
        
