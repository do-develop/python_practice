func sortMatrix(grid [][]int) [][]int {
    N := len(grid)

    // bottom-left triangle
    for i := 0; i < N; i++ {
        temp := []int{}
        for j := 0; i + j < N; j++ {
            temp = append(temp, grid[i+j][j])
        }
        sort.Sort(sort.Reverse(sort.IntSlice(temp)))
        for j := 0; i + j < N; j++ {
            grid[i+j][j] = temp[j]
        }
    }

    // top-right triangle
    for j := 1; j < N ; j++ {
        temp := []int{}
        for i := 0; i + j < N; i++ {
            temp = append(temp, grid[i][j+i])
        }
        sort.Ints(temp)
        for i := 0; i + j < N; i++ {
            grid[i][j+i] = temp[i]
        }
    }

    return grid
}