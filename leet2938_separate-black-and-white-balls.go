func minimumSteps(s string) int64 {
    var totalSwaps int64 = 0
    left := 0

    for right := range len(s) {
        if s[right] == '0' {
            totalSwaps += int64(right - left)
            left++
        }
    }
    return totalSwaps
}