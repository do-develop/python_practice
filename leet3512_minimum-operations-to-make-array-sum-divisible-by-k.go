func minOperations(nums []int, k int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total % k
}