func minimumAddedCoins(coins []int, target int) int {
    sort.Ints(coins)

    coinsAdded, reach, idx := 0, 0, 0
    for reach < target {
        if idx < len(coins) && coins[idx] <= reach + 1 {
            reach += coins[idx]
            idx++
        } else {
            coinsAdded++
            reach += reach + 1
        }
    }
    return coinsAdded
}