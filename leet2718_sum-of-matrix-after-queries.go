func matrixSumQueries(n int, queries [][]int) int64 {
    row := make(map[int]int)
    col := make(map[int]int)
    matSum := 0

    for i := len(queries) -1; i >= 0; i-- {
        t, idx, val := queries[i][0], queries[i][1], queries[i][2]

        if t == 0 {
            if _, exists := row[idx]; !exists {
                row[idx] = val
                matSum += val * (n - len(col))
            }
        } else if t == 1 {
            if _, exists := col[idx]; !exists {
                col[idx] = val
                matSum += val * (n - len(row))
            }
        }
    }
    return int64(matSum)
}