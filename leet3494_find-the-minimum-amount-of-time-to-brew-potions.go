func minTime(skill []int, mana []int) int64 {
    n, m := len(skill), len(mana)
    start := make([]int64, n)

    for j := 0; j < m; j++ {
        // wizard i can't start until wizard i-1 finishes
        for i := 1; i < n; i++ {
            start[i] = start[i-1] + int64(skill[i-1])*int64(mana[j])
        } 
        // start[0] + sum(skill[0..i-1])*mana[j+1] >= start[i] + skill[i]*mana[j]
        if j < m - 1 {
            var prefixSum int64
            var nextStart int64

            for i := 0; i < n; i++ {
                finishCurrent := start[i] + int64(skill[i])*int64(mana[j])
                // required_T + prefixSkill[i] * mana[j+1]  >=  finishCurrent
                required := finishCurrent - prefixSum*int64(mana[j+1])
                if required > nextStart {
                    nextStart = required
                }
                prefixSum += int64(skill[i])
            }
            start[0] = nextStart
        }
    }
    
    // the asnwer is when the last wiard finishes the last potion
    return start[n-1] + int64(skill[n-1])*int64(mana[m-1])
}