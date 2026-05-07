func hasSpecialSubstring(s string, k int) bool {
    N := len(s)
    i := 0

    for i < N {
        j := i

        for j < N && s[j] == s[i] {
            j++
        }
        if j - i == k {
            return true
        }
        i = j
    }
    return false
}