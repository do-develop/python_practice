func minDeletion(s string, k int) int {
    freq := make([]int, 26)
    for _, ch := range s {
        freq[ch - 'a']++
    } 

    // eliminate the character that appear the fewest times
    sort.Ints(freq)
    var dels int
    for i := 0; i < 26 - k; i++ {
        dels += freq[i]
    }
    return dels
}