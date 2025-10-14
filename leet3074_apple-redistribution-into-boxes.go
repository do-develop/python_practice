func minimumBoxes(apple []int, capacity []int) int {
    count, boxes := 0, 0

    for _, amt := range apple {
        count += amt
    }

    sort.Ints(capacity)
    for i := len(capacity) - 1; i >= 0 && count > 0; i-- {
        boxes++
        count -= capacity[i]
    }
    return boxes
}