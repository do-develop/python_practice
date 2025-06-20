func maximumOddBinaryNumber(s string) string {
    ones := strings.Count(s, "1")
    N := len(s)

    startingOnes := ones - 1
    newNumber := make([]byte, N)
    for i := 0; i < N; i++ {
        if i < startingOnes {
            newNumber[i] = '1'
        } else {
            newNumber[i] = '0'
        }
    }
    newNumber[N - 1] = '1'
    return string(newNumber)
}