func scoreBalance(s string) bool {
    sumR := make([]int, len(s))
    sumR[len(s) - 1] = int(s[len(s) - 1] - 'a') + 1
    for i := len(s) - 2; i >= 0; i-- {
        sumR[i] = sumR[i+1] + int(s[i]-'a') + 1
    }

    sumL := 0
    for i := 0; i < len(s) - 1; i++ {
        sumL += int(s[i] - 'a') + 1
        if sumL == sumR[i+1] {
            return true
        }
    }
    return false
}