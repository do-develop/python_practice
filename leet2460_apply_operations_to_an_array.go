func applyOperations(nums []int) []int { // simple simulation problem
    for i := 1; i < len(nums); i++ {
        if nums[i-1] == nums[i] {
            nums[i-1] = nums[i] * 2
            nums[i] = 0
        }
    }

    pos := 0 // latest position where 0 was found
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[i], nums[pos] = nums[pos], nums[i]
            pos++
        }
    }
    return nums
}