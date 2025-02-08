func maxScore(nums []int) int {
	var count int = 0
	var prefix int64 = 0
    // sort descending order
	sort.SliceStable(nums, func(x, y int) bool {
        return nums[x] > nums[y]
    })
    
    for _, num := range nums {
        prefix += int64(num)
        if prefix > 0 {
            count++
        } else {
            break
        }
    }
    return count
}