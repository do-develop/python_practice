class Solution:
    def largestInteger(self, num: int) -> int:
        even, odd = [], []
        nums = [int(x) for x in str(num)]
        for n in nums:
            if n % 2 == 0:
                heapq.heappush(even, -n)
            else:
                heapq.heappush(odd, -n)
        
        heapq.heapify(even)
        heapq.heapify(odd)
        res = []

        for n in nums:
            if n  % 2 == 0:
                res.append(str(-heapq.heappop(even)))
            else:
                res.append(str(-heapq.heappop(odd)))
        
        return int(''.join(res))
            
