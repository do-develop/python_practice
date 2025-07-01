func maximumTripletValue(nums []int) int64 {
    N := len(nums)
    maxRight := make([]int, N)
    maxRight[N - 1] = nums[N - 1]
    for i := N - 2; i >= 0; i-- {
        maxRight[i] = max(nums[i], maxRight[i + 1])
    }

    maxLeft := nums[0]
    var result int64 = 0
    for i := 1; i < N - 1; i++ {
        result = max(result, int64(maxLeft - nums[i]) * int64(maxRight[i + 1]))
        maxLeft = max(maxLeft, nums[i]) // update next maxLeft
    }

    return result
}