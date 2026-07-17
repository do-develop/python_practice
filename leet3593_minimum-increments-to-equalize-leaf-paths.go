func minIncrease(n int, edges [][]int, cost []int) int {
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }

    ans := 0

    var dfs func(node, parent int) int 
    dfs = func(node, parent int) int {
        maxVal := 0
        hasChild := false
        childVals := []int{}

        for _, next := range adj[node] {
            if next == parent {
                continue
            }

            hasChild = true
            v := dfs(next, node)
            childVals = append(childVals, v)
            if v > maxVal {
                maxVal = v
            }
        }

        if !hasChild {
            return cost[node]
        }

        for _, v := range childVals {
            if v != maxVal {
                ans++
            }
        }

        return maxVal + cost[node]
    }
    dfs(0, -1)
    return ans
}