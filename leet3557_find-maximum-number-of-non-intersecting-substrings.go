func maxSubstrings(word string) int {
    // greedy approach
    count := 0
    arr := make([]int, 26)
    for i := range arr {
        arr[i] = -1
    }

    for i, ch := range word {
        idx := ch - 'a'
        if arr[idx] != -1 && i - arr[idx] + 1 >= 4 {
            count++
            // reset arr
            for j := range arr {
                arr[j] = -1
            }
        } else if arr[idx] == -1 {
            arr[idx] = i
        }
    }
    return count
}