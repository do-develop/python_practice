func constructProductMatrix(grid [][]int) [][]int {
    rows, cols := len(grid), len(grid[0])
    mod := 12345
    pMatrix := make([][]int, rows)
    prod := 1

    for r := 0; r < rows; r++ {
        pMatrix[r] = make([]int, cols)
        for c := 0; c < cols; c++ {
            prod = prod * grid[r][c] % mod
            pMatrix[r][c] = prod
        }
    }

    suffixProd := 1
    for r := rows - 1; r >= 0; r-- {
        for c := cols - 1; c >= 0; c-- {
            prefixProd := 1
            if c > 0 {
                prefixProd = pMatrix[r][c - 1]
            } else if r > 0 {
                prefixProd = pMatrix[r - 1][cols - 1]
            }

            pMatrix[r][c] = prefixProd * suffixProd % mod
            suffixProd = suffixProd * grid[r][c] % mod
        }
    }
    return pMatrix
}