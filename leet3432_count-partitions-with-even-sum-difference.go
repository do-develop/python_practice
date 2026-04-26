func countPartitions(nums []int) int {
    totalSum := 0

    for _, n := range nums {
        totalSum += n
    }

    if totalSum % 2 == 0 {
        return len(nums) - 1
    }
    return 0
}