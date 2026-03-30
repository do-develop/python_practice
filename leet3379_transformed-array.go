func constructTransformedArray(nums []int) []int {
    N := len(nums)
    ans := make([]int, N)
    for i, val := range nums {
        ans[i] = nums[((i + val) % N + N) % N]
    }
    return ans
}