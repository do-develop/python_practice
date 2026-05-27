func numberOfComponents(properties [][]int, k int) int {
    N := len(properties)

    sets := make([]map[int]struct{}, N)
    for i, row := range properties {
        sets[i] = make(map[int]struct{})
        for _, v := range row {
            sets[i][v] = struct{}{}
        }
    }

    parent := make([]int, N)
    for i := range parent {
        parent[i] = i
    }

    var find func(x int) int
    find = func(x int) int {
        for parent[x] != x {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    union := func(x, y int) bool {
        px, py := find(x), find(y)
        if px == py {
            return false
        }
        parent[px] = py
        return true
    }

    components := N 
    for i := 0; i < N; i++ {
        for j := i+1; j < N; j++ {
            count := 0
            for v := range sets[i] {
                if _, ok := sets[j][v]; ok {
                    count++
                }
                if count >= k {
                    break
                }
            }
            // union if intersection ≥ k
            if count >= k {
                if union(i, j) {
                    components--
                }
            }
        }
    }
    return components
}