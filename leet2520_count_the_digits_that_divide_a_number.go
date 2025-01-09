func countDigits(num int) int {
    count, temp := 0, num

    for temp > 0 {
        digit := temp % 10
        temp /= 10
        if num % digit == 0 {
            count++
        }
    }
    return count
}