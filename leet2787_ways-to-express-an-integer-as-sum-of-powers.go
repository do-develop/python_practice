func numberOfWays(n int, x int) int {
    nums := []int{}
    k := 1

    for true {
        curr := int(math.Pow(float64(k), float64(x)))
        if curr > n {
            break
        }
        nums = append(nums, curr)
        k++
    }

    target := n
    dp := make([]int, target + 1) // number of ways to form the sum 
    dp[0] = 1

    for _, num := range nums {
        for j := target; j >= num; j-- {
            if num <= j {
                dp[j] = (dp[j-num] + dp[j]) % 1000000007
            }
        }
    }
    return dp[target]
}