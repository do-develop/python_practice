func minOperations(nums []int) int {
    ops := 0

    for _, n := range nums {
        if (n + ops) % 2 == 0 {
            ops++
        }
    }
    return ops
}