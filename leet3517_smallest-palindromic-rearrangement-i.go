func smallestPalindrome(s string) string {
    N := len(s)
    if N == 1 {
        return s
    }

    mid := int(N / 2)
    half := s[:mid]
    runes := []rune(half)

    slices.Sort(runes)
    ans := string(runes)
    slices.Reverse(runes)
    
    if N % 2 == 0 {
        return ans + string(runes)
    }
    return ans + string(s[mid]) + string(runes)
}