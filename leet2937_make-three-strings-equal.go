func findMinimumOperations(s1 string, s2 string, s3 string) int {
    idx := 0
    miniLen := min(len(s1), len(s2), len(s3))
    for idx < miniLen && s1[idx] == s2[idx] && s2[idx] == s3[idx] {
        idx++
    }
    if idx == 0 { return -1}

    return len(s1) + len(s2) + len(s3) - 3 * idx
}