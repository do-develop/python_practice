func maxProduct(nums []int) int64 {
    var a, b int
    for _, v := range nums {
        if abs(v) > a {
            a, b = abs(v), a
        } else if abs(v) > b {
            b = abs(v)
        }
    }

    return int64(a) * int64(b) * 100000
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}