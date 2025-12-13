func countCompleteDayPairs(hours []int) int {
    remainderCount := make(map[int]int)
    pairs := 0

    for _, hour := range hours {
        rem := hour % 24
        if rem == 0 {
            pairs += remainderCount[0]
        } else {
            pairs += remainderCount[24 - rem]
        }
        remainderCount[rem]++
    }
    return pairs
}