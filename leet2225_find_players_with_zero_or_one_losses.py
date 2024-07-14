class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        for match in matches:
            if match[-1] not in lost:
                lost[match[-1]] = 1
            else:
                lost[match[-1]] += 1
        
        hasnt_lost = set()
        for match in matches:
            if match[0] not in lost:
                hasnt_lost.add(match[0])
        
        lost_once = []
        for x in lost:
            if lost[x] == 1:
                lost_once.append(x)
        res = []
        hasnt_lost = list(hasnt_lost)
        hasnt_lost.sort()
        lost_once.sort()
        res.append(hasnt_lost)
        res.append(lost_once)
        return res
