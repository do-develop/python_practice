func minimumPartition(s string, k int) int {
    // Intuition: Greedy approach
    var num int64
    count := 1

    for i := 0; i < len(s); i++ {
        curr := int(s[i] - '0')
        if curr > k {
            return -1
        }

        num = num * 10 + int64(curr)
        if num > int64(k) { // need to split!
            num = int64(curr)
            count++
        }
    }
    return count
}