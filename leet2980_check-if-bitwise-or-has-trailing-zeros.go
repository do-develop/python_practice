func hasTrailingZeros(nums []int) bool {
    // need to find at least 2 even numbers
    foundEven := false

    for _, num := range nums {
        if num % 2 != 0 {
            continue
        }
        if foundEven {
            return true
        }
        foundEven = true
    }
    return false
}