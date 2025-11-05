func minRectanglesToCoverPoints(points [][]int, w int) int {
    xVals := make([]int, len(points))
    for i, p := range points {
		xVals[i] = p[0]
	}

    sort.Ints(xVals)
    count := 0
    last := -1

    for i := 0; i < len(xVals); i++ {
        if xVals[i] > last {
            count++
            last = xVals[i] + w
        }
    }
    return count
}