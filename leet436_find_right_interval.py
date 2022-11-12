class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return []
        elif len(intervals) == 1:
            return [-1]
        
        res = [-1] * len(intervals)
        dic = {i:intervals[i] for i in range(len(intervals))}
        dic_start = sorted(dic.items(), key=lambda x: x[1][0]) # sort by start
        dic_end   = sorted(dic.items(), key=lambda x: x[1][1]) # sort by end
        
        idx = 0
        for e in dic_end:
            i, interval = e
            while idx < len(intervals) and dic_start[idx][1][0] < interval[1]:
                idx += 1
            if idx == len(intervals):
                return res            
            res[i] = dic_start[idx][0]
        return res
