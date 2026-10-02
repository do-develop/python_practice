func findMissingElements(nums []int) []int {
    slices.Sort(nums)
    ans := []int{}

    for i := 0; i < len(nums) - 1; i++ {
        for candidate := nums[i] + 1; candidate < nums[i+1]; candidate++ {
            ans = append(ans, candidate)
        }
    }
    return ans
}