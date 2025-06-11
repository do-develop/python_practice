func minimumOperations(num string) int {
    minOps := len(num) // removing all digits
    cnt0, cnt5 := 0, 0

    for i := len(num) - 1; i >= 0; i-- {
        switch num[i] {
            case '0':
                cnt0++
                if cnt0 == 2 {
                    return len(num) - i - 2
                }
            case '5':
                cnt5++
                if cnt0 == 1 {
                    return len(num) - i - 2
                }
            case '2', '7':
                if cnt5 > 0 {
                    return len(num) - i - 2
                }
        }
    }
    return minOps - cnt0
}