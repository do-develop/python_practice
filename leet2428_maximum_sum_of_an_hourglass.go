func maxSum(grid [][]int) int {
    maxTotal := 0

    for i := 0; i < len(grid); i++ {
        if i + 2 < len(grid) {
            for j := 0; j < len(grid[i]); j++ {
                if j + 2 < len(grid[i]) {
                    total := grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+ grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                    if total > maxTotal {
                        maxTotal = total
                    }
                } else {
                    break
                }

            }
        } else {
            break
        }
    }
    return maxTotal
}