func bestHand(ranks []int, suits []byte) string {
    var best, suitsCount int
    var ranksFreq [14]int /// ranks between 1 ~ 13
    for i := 0; i < len(ranks); i++ {
        if suits[i] == suits[0] {
            suitsCount++
        }

        ranksFreq[ranks[i]]++
        if ranksFreq[ranks[i]] > best {
            best = ranksFreq[ranks[i]]
        }
    }

    if suitsCount == 5 {
        best = suitsCount
    }

    switch best {
        case 5:
            return "Flush"
        
        case 3,4:
            return "Three of a Kind"

        case 2:
            return "Pair"
    }

    return "High Card"
}