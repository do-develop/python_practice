class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        N = len(nums)
        for i in range(N):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
            
        even.sort()
        odd.sort(reverse=True)
        result = []
        
        for e, o in zip(even, odd):
            result.append(e)
            result.append(o)
        
        if len(even) > len(odd):
            result.append(even[-1])
        if len(even) < len(odd):
            result.append(odd[-1])
        return result
