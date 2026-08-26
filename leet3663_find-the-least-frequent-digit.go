func getLeastFrequentDigit(n int) int {
    frequencies := [10]int{}
    
    for n > 0 {
        frequencies[n % 10]++
        n /= 10
    }

    ans, mini := -1, 1 << 31
    for digit, freq := range frequencies {
        if freq != 0 && freq < mini {
            mini = freq
            ans = digit
        }
    }
    return ans
}