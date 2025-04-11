func countServers(n int, logs [][]int, x int, queries []int) []int {
    indexedQueries := make([][3]int, len(queries))

    for i := 0; i< len(queries); i++ {
        indexedQueries[i] = [3]int{i, queries[i] - x, queries[i]}
    }   
    sort.Slice(indexedQueries, func(x, y int)bool{
        return indexedQueries[x][1] < indexedQueries[y][1] // sort by query start time
    })
    sort.Slice(logs, func(x, y int)bool{
        return logs[x][1] < logs[y][1] // sort by time
    })

    active := make(map[int]int)
    arr := make([]int, len(queries))
    left, right := 0, 0

    for i := 0; i < len(indexedQueries); i++ {
        idx, start, end := indexedQueries[i][0], indexedQueries[i][1], indexedQueries[i][2]

        for right < len(logs) && logs[right][1] <= end {
            active[logs[right][0]]++
            right++
        }

        for left < len(logs) && logs[left][1] < start {
            active[logs[left][0]]--
            if active[logs[left][0]] == 0 {
                delete(active, logs[left][0])
            }
            left++
        }
        arr[idx] = n - len(active)
    }
    return arr
}