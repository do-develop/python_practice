func minimumCost(nums []int) int {
    mini1, mini2 := math.MaxInt, math.MaxInt

    for i := 1; i < len(nums); i++ {
        if nums[i] < mini1 {
            mini1, mini2 = nums[i], mini1
        } else if nums[i] < mini2 {
            mini2 = nums[i]
        }
    }
    return nums[0] + mini1 + mini2
}