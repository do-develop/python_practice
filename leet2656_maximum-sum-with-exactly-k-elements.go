func maximizeSum(nums []int, k int) int {
    sort.Ints(nums)
    score := nums[len(nums) - 1]

    start, last := score + 1, score + k 
    for start < last {
        score += start
        start++
    }
    return score
}
