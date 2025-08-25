func incremovableSubarrayCount(nums []int) int {
    count := 0
    N := len(nums)

    for left := 0; left < N; left++ {
        for right := left; right < N; right++ {
            isIncreasing := true
            prev := -1 << 31 // minimum int value

            for idx := 0; idx < N; idx++ {
                if idx >= left && idx <= right {
                    continue // removal window
                }
                if nums[idx] <= prev {
                    isIncreasing = false
                    break
                }
                prev = nums[idx]
            }
            // remaining array strictly increasing?
            if isIncreasing {
                count++
            }
        }
    }
    return count
}