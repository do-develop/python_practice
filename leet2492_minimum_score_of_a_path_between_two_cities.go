type pair struct {
    node int
    score int
}

func minScore(n int, roads [][]int) int {
    graph := make([][]pair, n + 1)
    for _, road := range roads {
        graph[road[0]] = append(graph[road[0]], pair{road[1], road[2]})
        graph[road[1]] = append(graph[road[1]], pair{road[0], road[2]})
    }
    visited := make([]bool, n + 1)
    q := []int{1}
    ans := math.MaxInt

    for len(q) > 0 {
        currSize := len(q)
        for i := 0; i < currSize; i++ {
            curr := q[0]
            q = q[1:]
            for _, edge := range graph[curr]{
                if edge.score < ans {
                    ans = edge.score
                }
                if !visited[edge.node] {
                    visited[edge.node] = true
                    q = append(q, edge.node)
                }
            }
        }
    }
    return ans
}