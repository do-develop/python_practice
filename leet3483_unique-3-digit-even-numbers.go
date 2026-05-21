func totalNumbers(digits []int) int {
    seen := make(map[int]bool)
    N := len(digits)

    for i := 0; i < N; i++ {
        if digits[i] == 0 {
            continue // no leading zero
        }
        for j := 0; j < N; j++ {
            if j == i {
                continue
            }
            for k := 0; k < N ; k++ {
                if k == i || k == j {
                    continue
                }
                if digits[k] % 2 != 0 {
                    continue
                }
                num := digits[i] * 100 + digits[j] * 10 + digits[k]
                seen[num] = true
            }
        }
    }
    return len(seen)
}