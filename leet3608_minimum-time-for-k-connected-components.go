func minTime(n int, edges [][]int, k int) int {
    f := make([]int, n)
    for i := range f {
        f[i] = i
    }

    var find func(x int) int 
    find = func(x int) int {
        if f[x] != x {
            f[x] = find(f[x])
        }
        return f[x]
    }

    union := func(x, y int) bool {
        rx, ry := find(x), find(y)
        if rx == ry {
            return false
        }
        f[rx] = ry
        return true
    }

    sort.Slice(edges, func(i, j int) bool {
		return edges[i][2] > edges[j][2] // descending by weight
	})

    count := n
    for _, e := range edges {
        u, v, t := e[0], e[1], e[2]
        if union(u, v) {
            count--
        }
        if count < k {
            return t
        }
    }
    return 0
}