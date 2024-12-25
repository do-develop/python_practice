func bestClosingTime(customers string) int {
    maxScore, currScore, bestHour := 0, 0, -1

    for i := 0; i < len(customers); i++ {
        if customers[i] == 'Y'{
            currScore++
        } else {
            currScore--
        }

        if currScore > maxScore {
            maxScore = currScore
            bestHour = i
        }
    }
    return bestHour + 1
}