const inf = int64(1) << 62

func minArraySum(nums []int, k int) int64 {
    N := len(nums)
    prefix := make([]int64, N+1)
    
    // best total deleted so far
	dp := make([]int64, N+1)
    // to remember best pair
    minVal := make([]int64, k)
    for i := range minVal {
		minVal[i] = inf
	}
    minVal[0] = 0

    for i := 1; i <= N; i++ {
        prefix[i] = prefix[i-1] + int64(nums[i-1])

        r := prefix[i] % int64(k)
        
        dp[i] = dp[i-1]
        if minVal[r] != inf {
            if candidate := prefix[i] - minVal[r]; candidate > dp[i] {
                dp[i] = candidate
            }
        }

        val := prefix[i] - dp[i]
        if val < minVal[r] {
            minVal[r] = val
        }
    }

    return prefix[N] - dp[N]
}