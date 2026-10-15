func totalWaviness(num1 int, num2 int) int {
    getWaviness := func(x int) int {
        str := strconv.Itoa(x)
        waviness := 0

        for i := 1; i < len(str) - 1; i++ {
            isPeak := str[i] > str[i-1] && str[i] > str[i+1]
            isValley := str[i] < str[i-1] && str[i] < str[i+1]
            if isPeak || isValley {
                waviness++
            }
        }
        return waviness
    }

    total := 0
    for n := num1; n <= num2; n++ {
        total += getWaviness(n)
    }
    return total
}