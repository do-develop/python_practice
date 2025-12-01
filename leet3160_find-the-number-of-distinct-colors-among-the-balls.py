class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        N = len(queries)
        result = []
        colors = {}
        balls = {}

        for i in range(N):
            ball, color = queries[i]
            if ball in balls:
                prevColor = balls[ball]
                colors[prevColor] -= 1

                if colors[prevColor] == 0:
                    del colors[prevColor]
            
            balls[ball] = color
            colors[color] = colors.get(color, 0) + 1

            result.append(len(colors))
        
        return result
