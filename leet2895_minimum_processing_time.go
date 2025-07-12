func minProcessingTime(processorTime []int, tasks []int) int {
    slices.Sort(processorTime)
    // sort tasks descending order
    slices.SortFunc(tasks, func (x, y int) int {
        return y - x
    })

    longest := 0

    for i := range processorTime {
        // only need to check the longest task of the block --> i * 4
        longest = max(longest, processorTime[i] + tasks[i * 4])
    }
    return longest
}