func makeIntegerBeautiful(n int64, target int) int64 {
    var ans int64 = 0

    if getDigitSum(n) <= target {
        return ans
    }

    for i := 10; ;i *= 10 {
        ans = int64(i) - n % int64(i) // make right handside digit to 0
        if getDigitSum(n + ans) <= target {
            return ans
        }
    }
    return 0
}

func getDigitSum(n int64) int {
    digitSum := 0
    for num := n; num != 0; num /=10 {
        digitSum += int(num % 10)
    }
    return digitSum
}