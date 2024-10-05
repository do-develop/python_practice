func maximumGroups(grades []int) int {
    N := len(grades)
    count := 0

    for N > count {
        count++
        N -= count
    }
    return count
}