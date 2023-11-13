class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # a prefix sum array for candies count
        # maxDay = prefix[type+1]-1;
        # minDay = prefix[type]/capacity;
        # If, day lies between max and min day then query is true
        res = [False] * len(queries)
        presum = [0] + candiesCount[:]
        for i in range(1, len(presum)):
            presum[i] += presum[i - 1]
        
        for idx, val in enumerate(queries):
            candy_type, fav_date, capacity = val
            max_day = presum[candy_type + 1] - 1
            min_day = presum[candy_type] // capacity
            if min_day <= fav_date <= max_day:
                res[idx] = True
        
        return res
