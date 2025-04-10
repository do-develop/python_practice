func longestSquareStreak(nums []int) int {
    sort.Ints(nums)
    numSet := make(map[int] bool)
    for _, num := range nums {
        numSet[num] = true
    }

    maxLength := -1
    for _, num := range nums {
        length := 0
        current := num

        for numSet[current] {
            length++
            current *= current
            if current > 1e9 { // problem constraints
                break
            }
        }

        if length >= 2 && length > maxLength {
            maxLength = length
        }
    }
    return maxLength
}