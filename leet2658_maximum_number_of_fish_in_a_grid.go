func findMaxFish(grid [][]int) int {
    rows := len(grid)
    cols := len(grid[0])
    directions := [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

    visited := make([][]bool, rows)
    for r := 0; r < rows; r++ {
        visited[r] = make([]bool, cols)
    }

    var dfs func(x, y int) int
    dfs = func(x, y int) int {
        if x < 0 || x >= rows || y < 0 || y >= cols || grid[x][y] == 0 || visited[x][y] {
            return 0
        }

        visited[x][y] = true
        fish := grid[x][y]
        for _, dir:= range directions {
            nx, ny := x + dir[0] , y + dir[1]
            fish += dfs(nx, ny)
        }
        return fish
    }

    maxFish := 0
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if grid[r][c] > 0 && !visited[r][c] {
                currSum := dfs(r, c)
                if currSum > maxFish {
                    maxFish = currSum
                }
            }
        }
    }
    return maxFish
}
