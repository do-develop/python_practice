func takeCharacters(s string, k int) int {
    N := len(s)
    counter := make([]int, 3)

    for _, c := range s {
        counter[c - 'a']++
    }

    for i := 0; i < 3; i++ {
        if counter[i] < k {
            return -1
        } 
    }

    // Find the longest removal window
    window := make([]int, 3)
    left, maxWindow := 0, 0
    for right := 0; right < N; right++ {
        window[s[right] - 'a']++

        // Reduce the size of removal window
        for left <= right && (counter[0]-window[0] < k || counter[1]-window[1] < k || counter[2]-window[2] < k) {
            window[s[left] - 'a']--
            left++
        }
        

        if right - left + 1 > maxWindow {
            maxWindow = right - left + 1
        }
    }
    return N - maxWindow
}

