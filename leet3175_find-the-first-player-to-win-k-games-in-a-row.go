func findWinningPlayer(skills []int, k int) int {
    pos, won := 0, 0

    for i := 1; i < len(skills); i++ {
        if skills[pos] < skills[i] {
            pos = i
            won = 0
        }
        won++
        if won == k {
            break
        }
    }
    return pos
}