func smallestNumber(n int) int {
    i := 1
    for i < n {
        i = i * 2 + 1
    }

    return i
}