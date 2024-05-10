class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        pos = collections.defaultdict(list)
        res = [0] * len(arr)
        for i, v in enumerate(arr):
            pos[v].append(i)

        for x in pos:
            positions = pos[x]
            prefix = [0] * (len(positions) + 1)
            for i in range(len(positions)):
                prefix[i + 1] = prefix[i] + positions[i]
        
            for i, v in enumerate(positions):
                smaller = v * i - prefix[i]
                larger = ((prefix[len(positions)] - prefix[i]) - v * (len(positions) - i))
                res[v] = smaller + larger
    
        return res
