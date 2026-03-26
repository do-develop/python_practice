func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
    n := len(edges1) + 1
	m := len(edges2) + 1

	// Build graphs
	graphA := buildGraph(n, edges1)
	graphB := buildGraph(m, edges2)

	// Step 1: count reachable nodes in A within distance k
	countA := make([]int, n)
	for i := 0; i < n; i++ {
		countA[i] = bfs(graphA, i, k)
	}

	// Step 2: count reachable nodes in B within distance k-1
	bestB := 0
	for i := 0; i < m; i++ {
		cnt := bfs(graphB, i, k-1)
		if cnt > bestB {
			bestB = cnt
		}
	}

	// Step 3: combine
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = countA[i] + bestB
	}

	return ans
}

func buildGraph(n int, edges [][]int) [][]int {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	return graph
}

func bfs(graph [][]int, start int, maxDist int) int {
	if maxDist < 0 {
		return 0
	}

	visited := make([]bool, len(graph))
	queue := []int{start}
	visited[start] = true

	dist := 0
	count := 1 // include itself

	for len(queue) > 0 {
		if dist == maxDist {
			break
		}

		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]

			for _, nei := range graph[node] {
				if !visited[nei] {
					visited[nei] = true
					queue = append(queue, nei)
					count++
				}
			}
		}
		dist++
	}

	return count
}