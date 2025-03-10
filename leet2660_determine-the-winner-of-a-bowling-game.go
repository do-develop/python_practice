func isWinner(player1 []int, player2 []int) int {
    score1 := calculateScore(player1)
    score2 := calculateScore(player2)

    if score1 > score2 {
        return 1
    } else if score1 < score2 {
        return 2
    } else {
        return 0
    }
}

func calculateScore(score []int) int {
    total := 0
    N := len(score)
    for i := 0; i < N; i++ {
        if i >= 1 && score[i-1] == 10 || i >= 2 && score[i-2] == 10 {
            total += 2 * score[i]
        } else {
            total += score[i]
        }
    }
    return total
}
