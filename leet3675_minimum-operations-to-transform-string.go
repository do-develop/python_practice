func minOperations(s string) int {
    arr := []byte(s)
    N := len(arr)
    ops := 0

    for i := 0; i < N; i++ {
        curr := (26 - (arr[i] - 'a')) % 26
        if int(curr) > ops {
            ops = int(curr)
        }
    }
    return ops
}