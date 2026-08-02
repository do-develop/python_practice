func countTrapezoids(points [][]int) int {
    mod := 1000000007
    pointsAtHeight := make(map[int]int)
    ans, sum := 0, 0

    for _, point := range points {
        y := point[1]
        pointsAtHeight[y]++
    }

    for _, pCount := range pointsAtHeight {
        // number of edges can be formed at this height
        edge := pCount * (pCount - 1) / 2 
        ans = (ans + edge * sum) % mod
        sum = (sum + edge) % mod
    }

    return ans
}