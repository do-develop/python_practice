func minMaxDifference(num int) int {
    numString := strconv.Itoa(num)
    maxString := numString
    for _, digit := range numString {
        if digit != rune('9') {
            maxString = strings.ReplaceAll(numString, string(digit), "9")
            break
        }
    }

    maxNum, _ := strconv.Atoi(maxString)
    minString := numString
    for _, digit := range numString {
        if digit != rune('0') {
            minString = strings.ReplaceAll(numString, string(digit), "0")
            break
        }
    }
    minNum, _ := strconv.Atoi(minString)
    return maxNum - minNum
}