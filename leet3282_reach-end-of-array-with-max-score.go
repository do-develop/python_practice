func findMaximumScore(nums []int) int64 {
    var score, curr int64

    for _, n := range nums {
        score += curr
        curr = max(curr, int64(n))
    }
    return score
}