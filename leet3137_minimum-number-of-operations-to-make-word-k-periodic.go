func minimumOperationsToMakeKPeriodic(word string, k int) int {
    N := len(word)
    count := make(map[string]int)

    for i := k ; i <= N; i += k {
        count[word[i - k : i]]++
    }

    var mx int

    for _, cnt := range count {
        mx = max(mx, cnt)
    }

    return N / k - mx
}