func maximumLengthSubstring(s string) int {
    counter := [26]int{}
    maxLen, N := 0, len(s)

    for l, r := 0, 0; r < N; {
        if counter[s[r] - 'a'] <  2 {
            counter[s[r] - 'a']++
            maxLen = max(maxLen, (r - l) + 1)
            r++
        } else {
            counter[s[l] - 'a']--
            l++
        }
    }

    return maxLen
}