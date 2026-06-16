func minOperations(nums []int) int {
    // the last element of each active increasing run
    tails := []int{}
    ops := 0

    for _, n := range nums {
        for len(tails) > 0 && tails[len(tails)-1] > n {
            tails = tails[:len(tails) - 1]
        }
        if n == 0 {
            continue
        }
        if len(tails) == 0 || tails[len(tails)-1] < n {
            ops++
            tails = append(tails, n)
        }
    }
    return ops
}