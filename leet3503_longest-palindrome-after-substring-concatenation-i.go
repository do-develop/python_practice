func longestPalindrome(s string, t string) int {
    expandAroundCenter := func(s string, left, right int) int {
        for left >= 0 && right < len(s) && s[left] == s[right] {
            left--
            right++
        }

        return right - left - 1
    }

    maxLength := 0
    n, m := len(s), len(t)

    for i := 0; i <= n; i++ {
        for j := 0; j <= m; j++ {
            combined := s[:i] + t[j:]

            for center := range combined {
                length1 := expandAroundCenter(combined, center, center)
                length2 := expandAroundCenter(combined, center, center+1)

                if length1 > maxLength { maxLength = length1 }
                if length2 > maxLength { maxLength = length2 }
            }
        }
    }
    return maxLength
}