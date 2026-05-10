func maxSubstringLength(s string, k int) bool {
    N := len(s)
    first := make([]int, 26)
    last := make([]int, 26)
    for i := range first { first[i] = N }
    for i := range last  { last[i] = -1 }

    seenOrder := []byte{}
    for i := 0; i < N; i++ {
        c := s[i] - 'a'
        if first[c] == N {
            first[c] = i
            seenOrder = append(seenOrder, s[i])
        }
        last[c] = i
    }

    // Merge overlapping intervals
    for _, ch := range seenOrder {
        c := ch - 'a'
        for j := first[c]; j < last[c]; j++ {
            x := s[j] - 'a'
            if first[x] < first[c] { first[c] = first[x] }
            if last[x]  > last[c]  { last[c]  = last[x]  }
        }
    }

    dp := make([]int, N+1)
    for i := 0; i < N; i++ {
        c := s[i] - 'a'
        // case 1: don't end a special substring here
        dp[i+1] = dp[i]

        // case 2: valid substring ends at i
        if last[c] == i && !(first[c] == 0 && i == N-1) {
            val := 1 + dp[first[c]]
            if val > dp[i+1] {
                dp[i+1] = val
            }
        }
    }

    return dp[N] >= k    
}