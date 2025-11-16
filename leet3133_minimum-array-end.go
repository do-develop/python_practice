func minEnd(n int, x int) int64 {
    last := x
    // Iterate n-1 times (since we already initialized result with x)
    for i := 1; i < n; i++ {
        // force the new number to keep the bit pattern of x by applying a bitwise OR with x
        last = (last + 1) | x
    }
    return int64(last)
}