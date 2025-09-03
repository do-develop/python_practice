func minOperations(nums []int, k int) int {
    finalXor := 0

    for _, n := range nums {
        finalXor ^= n
    }

    // number of different bits between two integers is just the number of set bits in (x XOR y)
    diff := finalXor ^ k
    count := 0
    for diff > 0 {
        count += diff & 1 // check the rightmost bit of diff
        diff >>= 1
    }

    return count
}