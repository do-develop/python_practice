func canAliceWin(nums []int) bool {
    var digit1, digit2 int

    for _, n := range nums {
        if n < 10 {
            digit1 += n
        } else {
            digit2 += n
        }
    }

    return digit1 != digit2
}