func recoverOrder(order []int, friends []int) []int {
    res := make([]int, 0)

    for _, val := range order {
        if slices.Contains(friends, val) {
            res = append(res, val)
        }
    }
    return res
}