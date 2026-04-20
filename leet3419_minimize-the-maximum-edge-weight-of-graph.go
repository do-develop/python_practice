func minMaxWeight(n int, edges [][]int, threshold int) int {
    // binary search
    // reverse edges, BFS from 0, ensure every non-zero node is reachable.

    revAdj := make([][][2]int, n)
    maxW := 0

    for _, e := range edges {
        from, to, w := e[0], e[1], e[2]
        revAdj[to] = append(revAdj[to], [2]int{from, w})
        if w > maxW {
            maxW = w
        }
    }

    // Check if all conditions with edges of weight <= limit
    canDo := func(limit int) bool {
        outDegree := make([]int, n)
        visited := make([]bool, n)
        queue := []int{0}
        visited[0] = true

        for len(queue) > 0 {
            cur := queue[0]
            queue = queue[1:]

            for _, next := range revAdj[cur] {
                neighbor, w := next[0], next[1]
                if w > limit || visited[neighbor] {
                    continue
                }

                outDegree[neighbor]++
                if outDegree[neighbor] > threshold {
					continue
				}
                visited[neighbor] = true
                queue = append(queue, neighbor)
            }
        }

        for i := 1; i < n; i++ {
            if !visited[i] {
				return false
			}
        }
        return true
    }

    // Binary search on the maximum edge weight
    lo, hi, ans := 1, maxW, -1
    for lo <= hi {
        mid := (lo + hi) / 2
        if canDo(mid) {
            ans = mid
            hi = mid - 1
        } else {
            lo = mid + 1
        }
    }
    return ans
}