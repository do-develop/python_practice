func maximumHappinessSum(happiness []int, k int) int64 {
    sort.Slice(happiness, func(x, y int) bool {
        return happiness[x] > happiness[y]
    })

    var res int64 = 0
    for i := 0; i < len(happiness) && i < k; i++ {
        if happiness[i] <= i {
            break
        }
        res += int64(happiness[i] - i)
    }

    return res
}