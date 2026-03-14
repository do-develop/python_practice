func hasIncreasingSubarrays(nums []int, k int) bool {
    N := len(nums)
    count, prev, ans := 1, 0, 0

    for i := 1; i < N; i++ {
        if nums[i] > nums[i - 1] {
            count++
        } else {
            prev = count
            count = 1
        }

        ans = max(ans, min(prev, count))
        ans = max(ans, count/2)
    }
    return ans >= k
}
