func resultsArray(nums []int, k int) []int {
    if k == 1 {
        return nums
    }

    N := len(nums)
    result := make([]int, N - k + 1)

    for i := range result {
        result [i] = -1
    }

    consecutiveCount := 1
    for i := 0; i < N - 1; i++ {
        if nums[i] + 1 == nums[i + 1] {
            consecutiveCount++
        } else {
            consecutiveCount = 1 // reset
        }

        if consecutiveCount >= k {
            // i + 1 end of the consecutive streak
            // subarray length k
            // start index (i + 1) - k + 1
            result[i - k + 2] = nums[i + 1]
        }
    }
    return result
}