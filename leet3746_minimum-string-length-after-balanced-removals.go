func minLengthAfterRemovals(s string) int {
    count := 0

    for _, char := range s {
        if char == 'a' {
            count++
        } else {
            count--
        }
    }
    return max(count, -count)
}