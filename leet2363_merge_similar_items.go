func mergeSimilarItems(items1 [][]int, items2 [][]int) [][]int {
    valToWeight := make(map[int]int)
    for _, item := range(items1) {
        valToWeight[item[0]] += item[1]
    }

    for _, item := range(items2) {
        valToWeight[item[0]] += item[1]
    }

    ans := make([][]int, 0, len(valToWeight))
    for k, v := range valToWeight {
        ans = append(ans, []int{k, v})
    }

    sort.Slice(ans, func(i, j int) bool {
        return ans[i][0] < ans[j][0]
    })

    return ans
}
