func remainingMethods(n int, k int, invocations [][]int) []int {
    adj := map[int][]int{}
    for _, v := range(invocations) {
        adj[v[0]] = append(adj[v[0]],v[1])
    }

    within := map[int]bool{}
    res := []int{}
    stack := []int{k}

    for len(stack) > 0 {
        top := stack[len(stack) - 1]
        within[top] = true
        stack = stack[:len(stack) - 1]
        for _, v := range(adj[top]) {
            if !within[v] {
                stack = append(stack, v)
            }
        }
    }

    // case 1 - no node should be deleted
    for _, v := range(invocations) {
        if !within[v[0]] && within[v[1]] {
            curr := []int{}
            for i:= 0; i < n; i++ {
                curr = append(curr, i)
            }
            return curr
        }
    }

    // case 2 - return that is not within the suspicious group
    for i := 0 ; i < n ; i ++ {
        if !within[i] {
            res = append(res,  i)
        }
    }
    return res
}