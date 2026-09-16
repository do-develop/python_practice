func alternatingSum(nums []int) int {
    asum := 0
    for i := 0; i < len(nums); i++ {
        if i % 2 == 0 {
            asum += nums[i]
        } else {
            asum -= nums[i]
        }
    }

    return asum
}