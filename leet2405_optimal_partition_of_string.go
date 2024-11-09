func partitionString(s string) int {
    // sliding window approach
    l, r := 0, 0
    count := 1

    for r < len(s) {
        if strings.Contains(s[l:r], string(s[r])){
            count++
            l = r
        } else {
            r++
        }
    }
    return count
}