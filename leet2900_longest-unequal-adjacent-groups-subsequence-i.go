func getLongestSubsequence(words []string, groups []int) []string {
    var subseq []string
    prev := -1
    for i := 0; i < len(words); i++ {
        if groups[i] != prev {
            subseq = append(subseq, words[i])
            prev = groups[i]
        }
    }
    return subseq
}