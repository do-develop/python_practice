func closestMeetingNode(edges []int, node1 int, node2 int) int {
    reachable1 := BFS(edges, node1)
    reachable2 := BFS(edges, node2)

    minDistance := math.MaxInt
    nodeIdx := -1

    for i := 0; i < len(edges); i++ {
        len1, ok := reachable1[i]
        if !ok {
            continue
        }

        len2, ok := reachable2[i]
        if !ok {
            continue
        }

        maxLen := max(len1, len2)
        if maxLen < minDistance {
            minDistance = maxLen
            nodeIdx = i
        }

    }
    return nodeIdx
}

func BFS(edges []int, node int) map[int]int {
    res := make(map[int]int)
    queue := []int{node}
    distance := 0

    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]

        res[curr] = distance
        next := edges[curr]
        _, visited := res[next]

        if next == -1 || visited {
            break
        }
        queue = append(queue, next)
        distance++
    }
    return res
}