class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rhombus = []
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                ans = grid[r][c]
                rhombus.append(grid[r][c])
                distance = 1
                while (r + distance < rows and c - distance >= 0 and c + distance < cols):
                    r1 = r + distance
                    c1 = c + distance
                    c2 = c - distance
                    ans += grid[r1][c1] + grid[r1][c2]
                    cur_sum = 0
                    while (True):
                        c1 -= 1
                        c2 += 1
                        r1 += 1
                        if (c1==0 or c2==cols or r1==rows): break
                        if (c1 == c2): # found the bottom point of rhombus
                            cur_sum += grid[r1][c1]
                            rhombus.append(ans + cur_sum)
                            break
                        cur_sum += grid[r1][c1] + grid[r1][c2]
                    distance += 1
        rhombus_list = list(set(rhombus))
        rhombus_list.sort(reverse=True)
        return rhombus_list[:3]
