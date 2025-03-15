func colorTheArray(n int, queries [][]int) []int {
    out := make([]int, len(queries))
    arr, count := make([]int, n), 0
    for i, query := range queries {
        index, color := query[0], query[1]
        prev, next := 0, 0
        if index > 0 {
            prev = arr[index - 1]
        }
        if index < n - 1 {
            next = arr[index + 1]
        }
        if arr[index] != 0 && arr[index] == prev {
            count--
        }
        if arr[index] != 0 && arr[index] == next {
            count--
        }
        arr[index] = color
        if arr[index] == prev {
            count++
        }
        if arr[index] == next {
            count++
        }
        out[i] = count
    }
    return out
}