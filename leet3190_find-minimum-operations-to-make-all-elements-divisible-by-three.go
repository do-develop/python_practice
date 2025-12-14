func minimumOperations(nums []int) int {
    total := 0

    for _, x := range nums {
        rem := x % 3
        total += min(rem, 3 - rem)
    }
    return total
}