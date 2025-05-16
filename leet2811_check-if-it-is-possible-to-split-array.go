func canSplitArray(nums []int, m int) bool {
    if len(nums) <= 2 {
        return true
    }
    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] + nums[i + 1] >= m {
            return true
        }
    }
    return false
}