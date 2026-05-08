func maxWeight(pizzas []int) int64 {
    sort.Ints(pizzas)
    N := len(pizzas)
    days := N / 4
    total := int64(0)
    idx := N - 1

    // process odd days first
    for day := 1; day <= days; day += 2 {
        total += int64(pizzas[idx])
        idx--
    }

    // pick the second heaviest on even days
    idx--
    for day := 2; day <= days; day += 2 {
        total += int64(pizzas[idx])
        idx -= 2
    }

    return total
}