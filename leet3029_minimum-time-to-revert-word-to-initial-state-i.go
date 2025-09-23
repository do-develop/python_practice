func minimumTimeToInitialState(word string, k int) int {
    suffix := word
    count := 0

    for len(suffix) >= k {
        count++

        suffix = suffix[k:]
        if suffix == word[:len(suffix)] {
            if len(word[len(suffix):]) % k == 0 {
                return count
            }
            return count + 1
        }
    }
    return count + 1
}