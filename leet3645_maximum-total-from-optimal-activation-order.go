func maxTotal(value []int, limit []int) int64 {
    groups := make(map[int][]int)
    for i, li := range limit {
        groups[li] = append(groups[li], value[i])
    }

    var total int64
    for li, values := range groups {
        slices.SortFunc(values, func(a, b int) int { return b - a}) // descending
        take := min(li, len(values))
        for i := 0; i < take; i++ {
            total += int64(values[i])
        }
    }
    return total
}