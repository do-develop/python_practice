func minimumOperationsToMakeEqual(x int, y int) int {
    if x <= y {
        return y - x
    }

    res := x - y

    for _, v := range []int{5, 11} {
        res = min(res, minimumOperationsToMakeEqual(x/v, y) + 1 + x%v)
        res = min(res, minimumOperationsToMakeEqual(x/v + 1, y) + 1 + v - x%v)
    }
    return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

