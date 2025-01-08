func maximumTastiness(price []int, k int) int {
    N := len(price)
    sort.Ints(price)

    start, end := 0, price[N-1] - price[0]
    res := 0

    for start <= end {
        mid := (start + end) / 2
        if isMatch(price, mid, k) {
            res = mid
            start = mid + 1
        } else {
            end = mid - 1
        }
    }
    return res
}

func isMatch(price []int, target, k int) bool {
    N := len(price)
    k--
    prev := price[0]
    for i := 1; k > 0 && i < N; i++ {
        // Is target the minimum difference for any subsequence of the array price?
        if price[i] - prev >= target {
            prev = price[i]
            k--
            if k == 0 {
                return true
            }
        }
    }
    return false
}