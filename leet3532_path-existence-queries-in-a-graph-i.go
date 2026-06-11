func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []bool {
    group := make([]int, n)
    groupID := 0

    for i := 1; i < n; i++ {
        if nums[i] - nums[i - 1] > maxDiff {
            groupID++
        }
        group[i] = groupID
    }

    answer := make([]bool, len(queries))
    for i, q := range queries {
        answer[i] = group[q[0]] == group[q[1]]
    }
    return answer
}