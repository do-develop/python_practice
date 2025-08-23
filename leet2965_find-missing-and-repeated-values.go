func findMissingAndRepeatedValues(grid [][]int) []int {
    N := len(grid)
    size := N * N
    freq := make([]int, size + 1)

    for _, row := range(grid) {
        for _, val := range(row) {
            freq[val]++
        }
    }

    a, b := -1, -1

    for num := 1; num <= size; num++ {
        if freq[num] == 2 {
            a = num
        } else if freq[num] == 0 {
            b = num
        }
    }
    return []int{a, b}
}