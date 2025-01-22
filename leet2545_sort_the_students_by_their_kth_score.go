func sortTheStudents(score [][]int, k int) [][]int {
    slices.SortFunc(score, func(x []int, y []int) int {
        if x[k] == y[k] {
            return 0
        } 
        if x[k] < y[k] { // descending order
            return 1
        }
        return -1
    })

    return score
}