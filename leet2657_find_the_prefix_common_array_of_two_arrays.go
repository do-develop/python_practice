func findThePrefixCommonArray(A []int, B []int) []int {
    N := len(A)
    seen := make(map[int]bool, N)
    res  := make([]int, N)
    counter := 0

    for i := 0; i < N; i++ {
        if seen[A[i]] {
            counter++
        } else {
            seen[A[i]] = true
        }
        if seen[B[i]] {
            counter++
        } else {
            seen[B[i]] = true
        }
        res[i] = counter
    }
    return res
}
