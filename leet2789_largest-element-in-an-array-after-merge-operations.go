func maxArrayValue(nums []int) int64 {
    maxVal, prev := 0, 0

    for i := len(nums) - 1; i >= 0; i-- {
        if prev >= nums[i] {
            prev += nums[i]
        } else {
            prev = nums[i]
        }
        if prev > maxVal {
            maxVal = prev
        }
    }
    return int64(maxVal)
}