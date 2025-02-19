func maximumCostSubstring(s string, chars string, vals []int) int {
    costs := make([]int, 26)

    for i := range costs {
        costs[i] = i + 1
    }

    for i := 0; i < len(chars); i++ {
        costs[chars[i] - 'a'] = vals[i]
    }

    // Kandane's Algorithm
    currMax, maxSum := 0,0
    for i := 0; i < len(s); i++ {
        currMax += costs[s[i] - 'a']
        if currMax < 0 {
            currMax = 0
        }

        if currMax > maxSum {
            maxSum = currMax
        }
    }
    return maxSum
}