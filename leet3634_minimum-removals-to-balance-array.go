func minRemoval(nums []int, k int) int {
    N := len(nums)
    sort.Ints(nums)

    ans := N
    right := 0 

    for left := 0; left < N; left++ {
        for right < N && int64(nums[right]) <= int64(nums[left]) * int64(k) {
            right++
        }
        current := N - (right - left)
        if current < ans {
            ans = current
        }
    }
    return ans
}