func maxOperations(s string) int {
    countOne := 0
    ops, i := 0, 0

    for i < len(s) {
        if s[i] == '0' {
            for i + 1 < len(s) && s[i + 1] == '0' {
                i++
            }
            ops += countOne
        } else {
            countOne++
        }
        i++
    }
    return ops
}