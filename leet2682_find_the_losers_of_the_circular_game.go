func circularGameLosers(n int, k int) []int {
    gamers := make([]int, n)

    var nxt int
    for i := 1; gamers[nxt] == 0; i++ {
        gamers[nxt] = 1
        nxt = (nxt + (i * k)) % n
    }

    losers := []int{}
    for i := range gamers {
        if gamers[i] == 0 {
            losers = append(losers, i + 1)
        }
    }
    return losers
}