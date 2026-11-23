func mirrorDistance(n int) int {
    diff := n - reverse(n)
    if diff < 0 {
        return -diff
    }
    return diff
}

func reverse(n int) int {
    reversed := 0
    for n > 0 {
        reversed = reversed * 10 + n % 10
        n /= 10
    }
    return reversed
}