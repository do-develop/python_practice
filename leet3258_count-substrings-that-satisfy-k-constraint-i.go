func countKConstraintSubstrings(s string, k int) int {
    count, cnt0, cnt1 := 0, 0, 0
    l := -1

    for r := 0; r < len(s); r++ {
        if s[r] == '1' {
            cnt1++
        } else {
            cnt0++
        }

        for l <= r && cnt0 > k && cnt1 > k {
            l++
            if s[l] == '1' {
                cnt1--
            } else {
                cnt0--
            }
        } 
        count += r - l
    }

    return count
}