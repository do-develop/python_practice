func countSymmetricIntegers(low int, high int) int {
    count := 0

    for i := low; i <= high; i++ {
        if isSymmetric(i) {
            count++
        }
    }
    return count
}

func isSymmetric(x int) bool {
    s := strconv.Itoa(x)
    if len(s) % 2 != 0 {
        return false
    }

    sumL, sumR := 0, 0
    mid := len(s) / 2

    for i := 0; i < mid; i++ {
        sumL += int(s[i] - '0')
        sumR += int(s[i + mid] - '0')
    }
    return sumL == sumR
}