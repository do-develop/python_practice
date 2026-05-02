func maxDifference(s string) int {
    characters := make(map[rune]int)
    for _, c := range s {
        characters[c]++
    }

    maxOdd, minEven := 1, len(s)
    for _, val := range characters {
        if val % 2 == 1 {
            maxOdd = max(maxOdd, val)
        } else {
            minEven = min(minEven, val)
        }
    }
    return maxOdd - minEven
}