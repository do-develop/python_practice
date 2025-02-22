func miceAndCheese(reward1 []int, reward2 []int, k int) int {
    // Greedy approach
    diffs := make([]int, len(reward1))
    ans := 0

    for i := 0; i < len(reward1); i++ {
        diffs[i] = reward1[i] - reward2[i]
        ans += reward2[i]
    }

    sort.Slice(diffs, func(i, j int) bool {
        return diffs[i] > diffs[j]
    })

    for _, diff := range diffs[:k] {
        ans += diff
    }
    return ans
}