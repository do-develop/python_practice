func evenOddBit(n int) []int {
    even, odd := 0, 0
    
    pos := 0
    for n > 0 {
        if n % 2 == 1 { // current bit is 1
            if pos % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
        n /= 2
        pos++
    }

    return []int{even, odd}
}