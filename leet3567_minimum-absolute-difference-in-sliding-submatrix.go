func minAbsDiff(grid [][]int, k int) [][]int {
    Row, Col := len(grid), len(grid[0])
    res := make([][]int, Row - k + 1)
    for i := range res {
        res[i] = make([]int, Col - k + 1)
    }

    for r := 0; r + k <= Row; r++ {
        for c := 0; c + k <= Col; c++ {
            // every consecutive k×k submatrix
            kgrid := []int{}
            for x := r; x < r+k; x++ {
                for y := c; y < c+k; y++ {
                    kgrid = append(kgrid, grid[x][y])
                }
            }

            kmin := math.MaxInt
            sort.Ints(kgrid)
            for t := 1; t < len(kgrid); t++ {
                if kgrid[t] == kgrid[t-1] {
                    continue
                }
                kmin = min(kmin, kgrid[t]-kgrid[t-1])
            }
            if kmin != math.MaxInt {
                res[r][c] = kmin
            }
        }
    }
    return res
}