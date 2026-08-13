func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
    for top, bottom := x, x + k - 1; top < bottom; top, bottom = top+1, bottom-1 {
        for col := y; col < y + k; col++ {
            grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
        }
    }
    return grid
}