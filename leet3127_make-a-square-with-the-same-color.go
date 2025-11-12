func canMakeSquare(grid [][]byte) bool {
    starts := [][2]int{{0, 0}, {0, 1}, {1, 0}, {1, 1}}
    for _, start := range starts {
        whites, blacks := 0, 0

        for i := 0; i < 2; i++ {
            for j := 0; j < 2; j++ {
                row, col := start[0] + i, start[1] + j

                if grid[row][col] == 'W' {
                    whites++
                } else {
                    blacks++
                }
            }
        }

        if whites >= 3 || blacks >= 3 {
            return true
        }
    }
    return false
}