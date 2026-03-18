func canAliceWin(n int) bool {
    turn := 0
    for n >= 0 {
        n -= 10 - turn
        turn++
    }
    return turn & 1 == 0
}