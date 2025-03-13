func firstCompleteIndex(arr []int, mat [][]int) int {
    rows := len(mat)
    cols := len(mat[0])

    rowCount := make([]int, rows)
    colCount := make([]int, cols)

    numPosition := make(map[int][2]int)
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            numPosition[mat[r][c]] = [2]int{r, c}
        }
    }

    for i, num := range arr {
        pos := numPosition[num]
        r, c := pos[0], pos[1]

        rowCount[r]++
        colCount[c]++

        if rowCount[r] == cols || colCount[c] == rows {
            return i
        }
    }
    return -1
}
