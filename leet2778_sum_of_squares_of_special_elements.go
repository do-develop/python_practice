func sumOfSquares(nums []int) int {
    total := 0
    N := len(nums)

    for i := 1; i <= N; i++ { // 1-indexed
        if N % i == 0 {
            total += nums[i - 1] * nums[i - 1]
        }
    }
    return total
}