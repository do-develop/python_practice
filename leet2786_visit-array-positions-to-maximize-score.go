func maxScore(nums []int, x int) int64 {
    N := len(nums)
    oddScore, evenScore := 0, 0
    best := 0

    for i := N - 1; i >= 0; i-- {
        if nums[i] % 2 == 1 {
            oddScore = nums[i] + max(oddScore, evenScore - x)
            best = oddScore
        } else {
            evenScore = nums[i] + max(evenScore, oddScore - x)
            best = evenScore
        }
    }
    return int64(best)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}