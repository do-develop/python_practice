func isGood(nums []int) bool {
    sort.Ints(nums)
    target := len(nums) - 1

    if nums[target] != target {
        return false
    }

    for i := 0; i < target; i++ {
        if nums[i] != i + 1 {
            return false
        }
    }
    return true
}