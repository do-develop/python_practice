func distinctAverages(nums []int) int {
    slices.Sort(nums)
    numExist := make(map[float64]bool)

    for i, j := 0, len(nums) - 1; i < j; i, j = i + 1, j - 1 {
        numExist[float64(nums[i] + nums[j])/2] = true
    }
    return len(numExist)
}