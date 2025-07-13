func minOperations(s1 string, s2 string, x int) int {
    N := len(s1)
    var diffs []int

    // Build list of differences
    for i := 0; i < N; i++ {
        if s1[i] != s2[i] {
            diffs = append(diffs, i)
        }
    }

    // Edge case - if odd number of difference, it is impossible
    if len(diffs) % 2 == 1 {
        return -1 
    }

    // Memoization map[i] -> best cost uo to diffs[i]
    cache := make(map[int]float64)

    var bestCostUpTo func(i int) float64
    bestCostUpTo = func(i int) float64 {
        if val, exists := cache[i]; exists {
            return val
        }

        var result float64

        switch i {
            case -1:
                result = 0
            case 0:
                result = float64(x) / 2
            default:
                // Split the current bit with a far bit
                opt1 := bestCostUpTo(i-1) + float64(x) / 2
                // Pair it with the previous mismatch at i-1
                opt2 := bestCostUpTo(i-2) + float64(diffs[i] - diffs[i-1])
                if opt1 < opt2 {
                    result = opt1
                } else {
                    result = opt2
                }
        }
        cache[i] = result
        return result
    }

    return int(bestCostUpTo(len(diffs) - 1))
}