func maxActiveSectionsAfterTrade(s string) int {
    n := len(s)
    ans := 0
    for _, c := range s {
        if c == '1' {
            ans++
        }
    }

    maxGain := 0
    leftZeroes := 0
    i := 0

    for i < n {
        ones := 0
        rightZeroes := 0

        for i < n && s[i] == '1'{
            ones++
            i++
        }

        for i < n && s[i] == '0' {
            rightZeroes++
            i++
        }

        if leftZeroes > 0 && ones > 0 && rightZeroes > 0 { 
            if leftZeroes+rightZeroes > maxGain {
                maxGain = leftZeroes + rightZeroes
            }
        }

        leftZeroes = rightZeroes
    }
    return ans + maxGain
}