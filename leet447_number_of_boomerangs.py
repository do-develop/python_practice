class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for x in points:
            hashmap = collections.defaultdict(int)
            for y in points:
                distance = pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)
                hashmap[distance] += 1
             # Sum the total number of combinations for the particular distance
            for dist in hashmap:
                count += hashmap[dist] * (hashmap[dist] - 1)
                
        return count
