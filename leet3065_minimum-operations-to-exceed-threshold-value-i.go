func minOperations(nums []int, k int) int {
    ops := 0
    for _, num := range nums {
        if num < k {
            ops++
        }
    }
    return ops
}