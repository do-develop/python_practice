func countElements(nums []int, k int) int {
    if k == 0 {
        return len(nums)
    }

    sort.Ints(nums)
    lastIdx := len(nums) - k - 1
    v := nums[lastIdx + 1]
    for lastIdx >= 0 && nums[lastIdx] == v {
        lastIdx--
    }
    return lastIdx + 1
}