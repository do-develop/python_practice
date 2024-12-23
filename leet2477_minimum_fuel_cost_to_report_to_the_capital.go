func minimumFuelCost(roads [][]int, seats int) int64 {
    graph := make([][]int, len(roads) + 1)
    for _, e := range roads {
        from, to := e[0], e[1]
        graph[from] = append(graph[from], to)
        graph[to] = append(graph[to], from)
    }

    var minCost int = 0
    calculateCost(0, -1, graph, seats, &minCost)
    return int64(minCost)
}

func calculateCost(curr int, parent int, graph [][]int, seats int, res *int) int {
    cost := 1

    for _, neigh := range graph[curr] {
        if neigh != parent {
            cost += calculateCost(neigh, curr, graph, seats, res)
        }
    }

    if curr != 0 {
        *res += (cost + seats - 1) / seats
    }
    return cost
}