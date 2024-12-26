func appendCharacters(s string, t string) int {
    // two pointers approach
    sizeS, sizeT := len(s), len(t)
    i, j := 0, 0
    for i < sizeS && j < sizeT {
        if s[i] == t[j] {
            j++
        }
        i++
    }
    return sizeT - j
}