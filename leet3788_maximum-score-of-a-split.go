func maximumScore(nums []int) int64 {
    var presum int
    N := len(nums);

    for i := 0; i < N - 1; i++ {
        presum += nums[i]
    }

    suffixMin := nums[N - 1]
    score := presum - suffixMin

    for i := N - 2; i > 0; i-- {
        suffixMin = min(suffixMin, nums[i])
        presum -= nums[i]
        if presum - suffixMin > score {
            score = presum - suffixMin
        }
    }
    return int64(score)
}