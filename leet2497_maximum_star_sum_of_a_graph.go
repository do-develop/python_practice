func maxStarSum(vals []int, edges [][]int, k int) int {
    graph := make([][]int, len(vals))
    for _, edge := range edges {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }

    maxSum := vals[0]
    for idx, neighbors := range graph {
        currSum := vals[idx]
        neighborsValues := make([]int, 0)
        for _, neigh := range neighbors {
            neighborsValues = append(neighborsValues, vals[neigh])
        }
        sort.Ints(neighborsValues)
        for i := len(neighborsValues) - 1; i >= 0; i-- {
            if (len(neighborsValues) - 1 - i) == k {
                break
            }
            if currSum + neighborsValues[i] > currSum {
                currSum += neighborsValues[i]
            }
        }
        if currSum > maxSum {
            maxSum = currSum
        }
    }
    return maxSum
}