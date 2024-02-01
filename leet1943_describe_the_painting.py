class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        colors = defaultdict(int)
        for start, end, color in segments:
            colors[start] += color
            colors[end] -=  color
        
        res, curr_color, parts = [], 0, sorted(colors.items())
        for pos in range(len(parts) - 1):
            curr_color += parts[pos][1] # color at this part
            if curr_color > 0:
                res.append([parts[pos][0], parts[pos+1][0], curr_color])
        return res
