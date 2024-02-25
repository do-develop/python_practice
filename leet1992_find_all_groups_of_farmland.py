class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res, R, C = [], len(land), len(land[0])

        def dfs(x, y):
            max_right_down = (x, y)
            land[x][y] = 0 # to mark as visited
            for dx, dy in [(1, 0), (0, 1)]:
                xx, yy = x + dx, y + dy
                if xx < R and yy < C and land[xx][yy] == 1:
                    max_right_down = max(dfs(xx, yy), max_right_down)
            return max_right_down
        
        for x, y in itertools.product(range(R), range(C)):
            if land[x][y] == 1:
                x2, y2 = dfs(x, y)
                res.append([x, y, x2, y2])
        return res
