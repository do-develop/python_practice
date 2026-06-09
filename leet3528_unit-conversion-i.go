func baseUnitConversions(conversions [][]int) []int {
    const MOD = int64(1e9 + 7)
    n := len(conversions) + 1

    // adjacency list [neighbor, factor]
    graph := make([][][2]int, n)
    for _, c := range conversions {
        src, dst, factor := c[0], c[1], c[2]
        graph[src] = append(graph[src], [2]int{dst, factor})
        graph[dst] = append(graph[dst], [2]int{src, factor})
    }

    result := make([]int, n)
    result[0] = 1 // 1 unit of type 0

    // BFS from node 0
    visited := make([]bool, n)
    q := []int{0}
    visited[0] = true

    for len(q) > 0 {
        node := q[0]
        q = q[1:]

        for _, edge := range graph[node] {
            neighbor, factor := edge[0], edge[1]
            if visited[neighbor] {
                continue
            }
            visited[neighbor] = true

            result[neighbor] = int((int64(result[node]) * int64(factor)) % MOD)
            q = append(q, neighbor)
        }
    }
    return result
}