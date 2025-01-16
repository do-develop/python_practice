func rangeAddQueries(n int, queries [][]int) [][]int {
    // Intuition => line sweep & prefix sum
    matrix := make([][]int, n)
    for i := 0; i < n; i++ {
        matrix[i] = make([]int, n)
    }

    for _, query := range queries {
        rowStart, colStart := query[0], query[1]
        rowEnd, colEnd := query[2], query[3]

        for i := rowStart; i <= rowEnd; i++ {
            matrix[i][colStart]++ // mark where to start
            if colEnd + 1 < n { // mark where to stop
                matrix[i][colEnd + 1]--
            }
        }
    }

    for r := 0; r < n; r++ {
        for c := 1; c < n; c++ {
            matrix[r][c] = matrix[r][c-1] + matrix[r][c]
        }
    }
    return matrix
}