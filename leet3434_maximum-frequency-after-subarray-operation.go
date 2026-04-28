func maxFrequency(nums []int, k int) int {
    totalK := 0
    for _, v := range nums {
        if v == k {
            totalK++
        }
    }

    bestGain := 0

    seen := make(map[int]bool)
    for _, v := range nums {
        if v != k {
            seen[v] = true
        }
    }

    // For each target value t != k, find the best subarray
    // where we convert t's into k's (gain +1) 
    // while avoiding displacing existing k's (loss -1).
    for t := range seen {
        gain := 0
        maxGain := 0

        for _, v := range nums {
            if v == t {
                gain++
            } else if v == k {
                gain--
            }

            if gain < 0 {
                gain = 0
            }
            if gain > maxGain {
                maxGain = gain
            }
        }

        if maxGain > bestGain {
            bestGain = maxGain
        }
    }

    return totalK + bestGain
}