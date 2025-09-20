func numberOfPairs(points [][]int) int {
    sort.Slice(points, func(i, j int) bool {
        if points[i][0] == points[j][0] {
            return points[i][1] > points[j][1] // y descending
        }
        return points[i][0] < points[j][0] // x ascending
    })

    N := len(points)
    result := 0

    for i := 0; i < N; i++ {
        top := points[i][1]
        bottom := -1 << 31 

        for j := i + 1; j < N; j++ {
            y := points[j][1]
            
            if bottom < y && y <= top {
                result++
                bottom = y
                if bottom == top {
                    break
                }
            }

        }
    }
    return result
}