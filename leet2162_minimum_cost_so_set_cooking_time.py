class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            if mins > 99 or secs > 99 or mins < 0 or secs < 0:
                return float('inf')
            timestr, curr, res = str(mins * 100 + secs), str(startAt), 0
            for char in timestr:
                if char == curr:
                    res += pushCost
                else:
                    res += (moveCost + pushCost)
                    curr = char
            return res
        
        '''
        maxmins, mincost = targetSeconds // 60, float('inf')
        for mins in range(maxmins + 1):
            secs = targetSeconds - (mins * 60)
            if secs > 99 or mins > 99: continue
            mincost  = min(mincost, cost(mins, secs))
        return mincost
        '''
        # maxmins - 2 already means 120 secs which is over 99
        # so there are only two cases to check
        maxmins, minsecs = targetSeconds // 60, targetSeconds % 60
        return min(cost(maxmins, minsecs), cost(maxmins - 1, minsecs + 60))
