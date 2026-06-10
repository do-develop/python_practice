func countCoveredBuildings(n int, buildings [][]int) int {
    maxRow := make([]int, n+1)
    minRow := make([]int, n+1)
	maxCol := make([]int, n+1)
	minCol := make([]int, n+1)

    for i := range minRow {
        minRow[i] = n + 1
        minCol[i] = n + 1
    }

    for _, pos := range buildings {
        x, y := pos[0], pos[1]
        maxRow[y] = max(maxRow[y], x) // rightmost in its row
        minRow[y] = min(minRow[y], x) // leftmost in its row
        maxCol[x] = max(maxCol[x], y) // topmost in its col
        minCol[x] = min(minCol[x], y) // bottommost in its col
    }

    count := 0
    for _, pos := range buildings {
        x, y := pos[0], pos[1]
        if x > minRow[y] && x < maxRow[y] &&
            y > minCol[x] && y < maxCol[x] {
                count++
        }
    }
    return count
}