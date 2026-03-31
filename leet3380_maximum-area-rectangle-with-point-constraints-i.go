func maxRectangleArea(points [][]int) int {
    sort.Slice(points, func(x, y int) bool {
        if points[x][0] == points[y][0] {
            return points[x][1] < points[y][1]
        } 
        return points[x][0] < points[y][0]
    })

    maxArea := -1
    for i := 0; i < len(points) - 2; i++ {
        if points[i][0] != points[i+1][0] {
            continue
        }

        for j := i + 2; j < len(points) - 1; j++ {
            inRange := points[j][1] >= points[i][1] && points[j][1] <= points[i+1][1]

            if inRange {
                rightPairAligned := points[j][0] == points[j+1][0]
                bottomMatch := points[j][1] == points[i][1]
                topMatch := points[j+1][1] == points[i+1][1]

                if rightPairAligned && bottomMatch && topMatch {
                    // All four corners match — compute and record the area.
                    width  := points[j][0] - points[i][0]
                    height := points[i+1][1] - points[i][1]
                    maxArea = max(maxArea, width*height)
                }
                break
            }

        }
    }
    return maxArea
}