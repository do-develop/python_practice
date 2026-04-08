func checkValidCuts(n int, rectangles [][]int) bool {
    checkCuts := func(dim int) bool {
        sort.Slice(rectangles, func(i, j int)bool {
            return rectangles[i][dim] < rectangles[j][dim]
        })

        gapCount := 0
        furthestEnd := rectangles[0][dim+2]

        for i := 1; i < len(rectangles); i++ {
            rect := rectangles[i]
            if furthestEnd <= rect[dim] {
                gapCount++
            }

            if rect[dim+2] > furthestEnd {
                furthestEnd = rect[dim + 2]
            }
        }
        return gapCount >= 2
    }
    return checkCuts(0) || checkCuts(1)
}