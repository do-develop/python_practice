func minimizeSum(nums []int) int {
    // Intuition:
    // Change two biggest or,
    // Change the biggest and the smallest or,
    // Change two smallest
    sort.Ints(nums)
    N := len(nums)

    minSum := nums[N - 3] - nums[0]
    if nums[N - 2] - nums[1] < minSum {
        minSum = nums[N - 2] - nums[1]
    }
    if nums[N - 1] - nums[2] < minSum {
        minSum = nums[N - 1] - nums[2]
    }
    return minSum
}