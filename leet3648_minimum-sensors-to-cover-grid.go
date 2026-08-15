func minSensors(n int, m int, k int) int {
    // arithmatic problem
    cover := (2 * k) + 1

    rCover := n / cover
    if n % cover > 0 {
        rCover++
    }

    cCover := m / cover
    if m % cover > 0 {
        cCover++
    }

    return rCover * cCover
}