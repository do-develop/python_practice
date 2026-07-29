func minCost(n int, edges [][]int, k int) int {
    if n <= k {
        return 0
    }

    roots := make([]int, n)
    for i := range roots {
        roots[i] = i
    }

    var find func(x int) int
    find = func(x int) int {
        if roots[x] != x {
            roots[x] = find(roots[x])
        }
        return roots[x]
    }

    union := func(x, y int) bool {
        x, y = find(x), find(y)
        if x == y {
            return false
        }
        roots[x] = y
        return true
    }

    sort.Slice(edges, func(i, j int)bool {
        return edges[i][2] < edges[j][2]
    })

    count := n
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        if union(u, v) {
            count--
        }
        if count <= k {
            return w
        }
    }

    return 0
}