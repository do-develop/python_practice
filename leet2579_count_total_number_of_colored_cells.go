func coloredCells(n int) int64 {
    colored := int64(1)

    for i := 0; i < n; i++ {
        colored += int64(4 * i)
    }

    return colored
}