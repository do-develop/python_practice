func findPermutationDifference(s string, t string) int {
    total := 0

    for _, ch := range s {
        posS := strings.IndexRune(s, ch)
        posT := strings.IndexRune(t, ch)
        diff := posS - posT
        if diff < 0 {
            diff = -diff
        }

        total += diff
    }
    return total
}