func partitionString(s string) []string {
    left := 0

    seen := make(map[string]bool)
    var result [] string
    for right := 0; right < len(s); right++ {
        curr := s[left : right + 1]
        if _, ok := seen[curr]; !ok {
            result = append(result, curr)
            left = right + 1
            seen[curr] = true
        }
    }
    return result
}