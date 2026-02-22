func maximumTotalSum(maximumHeight []int) int64 {
    N := len(maximumHeight) 

    sort.Slice(maximumHeight, func(i, j int) bool {
        return maximumHeight[i] < maximumHeight[j]
    })

    prev := maximumHeight[N - 1]
    var total int64 = 0

    total += int64(prev)
    for i := N - 2; i >= 0; i-- {
        x := min(prev - 1, maximumHeight[i])
        if x < 1 {
            return -1
        }
        total += int64(x)
        prev = x
    }

    return total
}