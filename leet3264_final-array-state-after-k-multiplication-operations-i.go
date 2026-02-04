func getFinalState(nums []int, k int, multiplier int) []int {
    for i := 0; i < k; i++ {
        minIdx := slices.Index(nums, slices.Min(nums))
        nums[minIdx] *= multiplier
    }
    return nums
}