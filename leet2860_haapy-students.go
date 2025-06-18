func countWays(nums []int) int {
    sort.Ints(nums)
    N := len(nums)
    total := 0

    // not selecting any one
    if 0 < nums[0] {
        total++
    }

    for i := 1; i < N; i++ {
        if i > nums[i - 1] && i < nums[i] {
            total++
        }
    }

    // all selected
    if N > nums[N - 1] {
        total++
    }
    return total
}