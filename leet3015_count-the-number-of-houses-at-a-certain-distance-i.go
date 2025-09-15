func countOfPairs(n int, x int, y int) []int {
    if x > y { x, y = y, x}

    res := make([]int, n)
    for i := 1; i <= n; i++ {
        for j := i + 1; j <= n; j++ {
            dist := min(j - i, 1 + abs(i - x) + abs(j - y))
            res[dist - 1] += 2 // -1 is because array indices start from 0
        }
    }
    return res
}

func min(a,b int) int {
    if a < b { return a }
    return b
}

func abs(a int) int {
    if a < 0 { return -a }
    return a
}
