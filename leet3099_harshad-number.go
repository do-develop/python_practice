func sumOfTheDigitsOfHarshadNumber(x int) int {
    sum := getSumOfDigits(x)

    if x % sum == 0 {
        return sum
    }
    return -1
}

func getSumOfDigits(x int) int {
    sum := 0
    for x > 0 {
        sum += x % 10
        x /= 10
    }

    return sum
}