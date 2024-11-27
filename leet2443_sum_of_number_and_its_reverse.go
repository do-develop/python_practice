func sumOfNumberAndReverse(num int) bool {
    if num == 0 {
        return true
    }

    for i := num/2; i <= num; i++ {
        reversed, temp := 0, i
        for temp > 0 {
            reversed, temp = reversed * 10 + temp % 10, temp / 10
        }

        if reversed + i == num {
            return true
        }
    }
    return false
}