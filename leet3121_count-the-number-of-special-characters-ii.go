func numberOfSpecialChars(word string) int {
    var lo, up [26]int
    for i := range len(lo) {
        lo[i] = -1
        up[i] = -1
    }

    for i, ch := range word {
        if unicode.IsLower(ch) {
            lo[ch -'a'] = i
        } else if up[ch -'A'] == -1 {
            up[ch -'A'] = i
        }
    }

    count := 0
    for i := 0; i < 26; i++ {
        if lo[i] != -1 && (lo[i] < up[i]){
            count++
        }
    }
    return count
}