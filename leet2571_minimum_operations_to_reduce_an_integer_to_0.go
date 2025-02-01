func minOperations(n int) int {
    count, ops := 0, 0

    for n > 0 {
        if n & 1 != 0 { // least significant bit is 1
            count++     // count all the separate bit
        } else if count == 1 {
            ops++       // remove operation
            count = 0
        } else if count > 1 {
            ops++       // merge continuous bits into 1 bit
            count = 1   // merged bit should carry to next position
        }
        n >>= 1
    }

    if count == 1 {
        ops++
    } else if count > 1 {
        ops += 2
    }
    return ops
}