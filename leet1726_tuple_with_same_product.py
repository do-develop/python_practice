class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        '''
        No of ways of arranging (a*b) = 2 {(a,b),(b,a)}
        No of ways of arranging (c*d) = 2 {(c,d),(d,c)}
        No of wasy of arranging (a*b) and (c*d) = 2  {(a*b)=(c*d), (c*d)=(a*b)}
        Hence the total no of ways = 2*2*2 =8 
        '''
        count = 0
        freq = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                key = nums[i] * nums[j]
                count += freq.get(key, 0)
                freq[key] = freq.get(key, 0) + 1
        return 8 * count
