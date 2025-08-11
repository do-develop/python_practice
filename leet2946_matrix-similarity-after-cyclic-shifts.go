func areSimilar(mat [][]int, k int) bool {
    for _, line := range mat {
        N := len(line)
        for i := 0; i < N; i++ {
            if line[i] != line[(i + k) % N] {
                return false
            }
        }
    }
    return true
}