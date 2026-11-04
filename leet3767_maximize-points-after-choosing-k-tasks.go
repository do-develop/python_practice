func maxPoints(technique1 []int, technique2 []int, k int) int64 {
    var sum int64 = 0
    var diffs [][]int

    for i := 0; i < len(technique1); i++ {
        if technique1[i] >= technique2[i] {
            sum += int64(technique1[i])
            k--
        } else {
            diffs = append(diffs, []int{technique2[i] - technique1[i], technique2[i], technique1[i]})
        }
    }

    sort.Slice(diffs, func(i, j int) bool {
        return diffs[i][0] < diffs[j][0]
    })

    idx := 0
    for k > 0 {
        sum += int64(diffs[idx][2])
        idx++
        k--
    }

    for i := len(diffs)-1; i >= idx; i-- {
        sum += int64(diffs[i][1])
    }
    return sum
}