func findCommonResponse(responses [][]string) string {
    dict := make(map[string][]int)

    for i, resp := range responses {
        for _, s := range resp {
            if len(dict[s]) == 0 || dict[s][len(dict[s])-1] != i {
                dict[s] = append(dict[s], i)
            }
        }
    }

    var common string
    var maxCount int

    for k, v := range dict {
        if len(v) == maxCount {
            if k < common { // lexicographically smallest 
                common = k
            }
        } else if len(v) > maxCount {
            maxCount = len(v)
            common = k
        }
    }
    return common
}