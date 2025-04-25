func maximumBeauty(nums []int, k int) int {
    // sort the array
    sort.Ints(nums)
    // sliding window to find the largest valid window
    maxBeauty := 0
    left := 0

    for right := 0; right < len(nums); right++ {
        for nums[right] - nums[left] > 2 * k {
            left++
        }
        maxBeauty = max(maxBeauty, right - left + 1)
    }
    return maxBeauty
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}