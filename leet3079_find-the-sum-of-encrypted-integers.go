func sumOfEncryptedInt(nums []int) int {
    sum := 0

    for _, n := range nums {
        sum += encrypt(n)
    }
    return sum
}

func encrypt(x int) int {
    maxDigit, pow := 0, 0

    for x > 0 {
        maxDigit = max(maxDigit, x % 10)
        x /= 10
        pow *= 10
        pow++
    }
    return maxDigit * pow
}