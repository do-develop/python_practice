func countMajoritySubarrays(nums []int, target int) int {
    N := len(nums)
    majority := 0

    for i := 0; i < N; i++ {
        curr := 0
        for j := i; j < N; j++ {
            if nums[j] == target {
                curr++
            } else {
                curr--
            }
            if curr > 0 {
                majority++
            }
        }
    }
    return majority
}