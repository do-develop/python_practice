func findChampion(grid [][]int) int {
    // assume player 0 is the champion
    winner := 0 
    N := len(grid)
    for opponent := range(N) {
        if opponent == winner {
            continue
        }
        // is current winner lost to the opponent
        if grid[winner][opponent] == 0 { 
            winner = opponent
        }
    }
    return winner
}