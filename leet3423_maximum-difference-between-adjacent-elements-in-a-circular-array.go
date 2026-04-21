func maxAdjacentDistance(nums []int) int {
    N := len(nums)
    dist := int(math.Abs(float64(nums[0] - nums[N-1])))
    for i := 0; i < N - 1; i++ {
        dist = int(math.Max(float64(dist), math.Abs(float64(nums[i] - nums[i+1]))))
    }
    return dist
}