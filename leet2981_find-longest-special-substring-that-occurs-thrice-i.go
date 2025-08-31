func maximumLength(s string) int {
    N := len(s)
    if N == 0 {
        return -1
    }

    freq := make(map[string]int)

    for length := 1; length <= N; length++ {
        for i := 0; i + length <= N; i++ {
            substr := s[i : i + length]
            char := substr[0]
            isSpecial := true
            for _, c := range substr {
                if byte(c) != char {
                    isSpecial = false
                    break
                }
            }
            if isSpecial {
                freq[substr]++
            }
        }
    }

    maxLen := -1
    for substr, cnt := range freq {
        if cnt >= 3 && len(substr) > maxLen {
            maxLen = len(substr)
        }
    }
    return maxLen
}