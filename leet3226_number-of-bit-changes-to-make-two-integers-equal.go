func minChanges(n int, k int) int {
    count  :=  0
    for k > 0 || n > 0 {
		// & 1 extracts the least significant bit
        if n & 1 == 1 && k & 1 == 0 {
            count++
        }
        if n & 1 == 0 && k & 1 == 1 {
            return -1
        }
        n >>= 1
        k >>= 1
    }
    return count
}