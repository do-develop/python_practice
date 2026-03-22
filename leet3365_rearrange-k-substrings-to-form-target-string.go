func isPossibleToRearrange(s string, t string, k int) bool {
    strCount := make(map[string]int)
    if len(s) % k != 0 {
        return false
    }

    subSize := int(len(s) / k)
    prev := 0

    for i := subSize; i <= len(s); i += subSize {
        strCount[s[prev:i]] += 1
        strCount[t[prev:i]] -= 1
        prev = i
    }

    for i := range strCount {
        if strCount[i] != 0 {
            return false
        }
    }
    return true
}