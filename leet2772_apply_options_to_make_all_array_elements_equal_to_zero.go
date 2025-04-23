func checkArray(nums []int, k int) bool {
    N := len(nums)
    memo := make([]int, k) // sliding window
    dec := 0

    for i := 0; i < N ; i++ {
        if i >= k {
            dec -= memo[i % k]
        }
        rem := nums[i] - dec

        if i <= N - k {
            if rem < 0 {
                return false
            }
            memo[i % k] = rem
            dec += rem
        } else {
            if rem != 0 {
                return false
            }
        }
    }
    return true
}