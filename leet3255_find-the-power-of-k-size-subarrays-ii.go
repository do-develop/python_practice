func resultsArray(nums []int, k int) []int {
    N := len(nums)
    pref := make([]int, N)
    length := 1

    pref[0] = 1

    for i := 1; i < N; i++ {
        if nums[i] - nums[i - 1] == 1 {
            length++
        } else {
            length = 1
        }
        pref[i] = length
    }

    result := make([]int, (N - k + 1))

    for i := k-1; i < N; i++ {
        if pref[i] >= k {
            result[i - (k - 1)] = nums[i]
        } else {
            result[i-(k - 1)] = -1
        }
    }
    return result
}