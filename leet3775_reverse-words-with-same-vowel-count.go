func reverseWords(s string) string {
    N := len(s)
    bytes := []byte(s)
    targetCount := -1

    for i := 0; i < N; i++ {
        curr := 0
        startIdx := i

        for ; i < N && s[i] != ' '; i++ {
            if isVowel(s[i]) {
                curr++
            }
        }

        if targetCount == -1 {
            targetCount = curr
        } else if curr == targetCount {
            // reverse the word
            for left, right := startIdx, i - 1; left < right; left, right = left + 1, right - 1 {
                bytes[left], bytes[right] = bytes[right], bytes[left]
            }
        }
    }
    return string(bytes)
}

func isVowel(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}