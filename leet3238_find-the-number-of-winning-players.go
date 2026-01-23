func winningPlayerCount(n int, pick [][]int) int {
    count := make([][]int, n)
    res := map[int]struct{}{}

    for _, p := range pick {
        if count[p[0]] == nil {
            count[p[0]] = make([]int, 11)
        }
        count[p[0]][p[1]]++
        if count[p[0]][p[1]] > p[0] {
            res[p[0]] = struct{}{}
        }
    }
    return len(res)
}