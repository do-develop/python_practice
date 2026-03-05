func numberOfSubstrings(s string, k int) int {
    N := len(s)
    var freq [26]int
    ans := 0
    left := 0
    countAtLeastK := 0

    for right := left; right < N; right++ {
        idx := s[right] - 'a'
        freq[idx]++

        if freq[idx] == k {
            countAtLeastK++
        }

        for countAtLeastK > 0 {
            ans += N - right

            leftIdx := s[left] - 'a'
            freq[leftIdx]--
            if freq[leftIdx] == k - 1 {
                countAtLeastK--
            }
            left++
        }
    }
    
    return ans
}