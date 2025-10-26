func minOperations(k int) int {
    num, ops := 1, math.MaxInt64

    if num >= k {
        return 0
    }

    currOps := 0
    for num <= k {
        add := 0

        if k % num > 0 {
            add++
        }

        ops = min(ops, currOps + k / num + add)
        currOps++
        num++
    }
    
    return ops - 1
}