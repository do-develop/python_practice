func edgeScore(edges []int) int {
    var maxScore int64 = math.MinInt64
    var ans int = math.MaxInt
    score := make([]int64, len(edges))

    for i:= 0; i < len(edges); i++ {
        score[edges[i]] += int64(i)
        if score[edges[i]] > maxScore {
            ans = edges[i]
            maxScore = score[edges[i]]
        } else if score[edges[i]] == maxScore {
            if edges[i] < ans {
                ans = edges[i]
            }
        }
    }
    return ans
}