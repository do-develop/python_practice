func findScore(nums []int) int64 {
	// sliding window approach
    var ans int64 = 0
    N := len(nums)

    for i := 0; i < N; i += 2{
        currentStart := i
        for i + 1 < N && nums[i] > nums[i + 1] {
            i++
        }
        currentPos := i
        for currentPos >= currentStart {
            ans += int64(nums[currentPos])
            currentPos -= 2
        }
    }
    return ans
}