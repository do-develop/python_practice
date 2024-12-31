func deleteGreatestValue(grid [][]int) int {  
    for i := 0; i < len(grid); i++ {
        slices.SortFunc(grid[i], func(a, b int)int {
            return b - a
        })
    }

    answer := 0
    for j := 0; j < len(grid[0]); j++ {
        slices.SortFunc(grid, func(a, b []int)int {
            return b[j] - a[j] 
        })
        answer += grid[0][j]
    }
    return answer
}