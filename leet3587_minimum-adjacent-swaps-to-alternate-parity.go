func minSwaps(nums []int) int {
    N := len(nums)
    oddCount := 0
    oddPos := make([]int, 0, N)

    for i, v := range nums {
        if v % 2 != 0 {
            oddCount++
            oddPos = append(oddPos, i)
        }
    }
    evenCount := N - oddCount

    if abs(evenCount - oddCount) > 1 {
        return -1
    }

    cost := func(oddAtEvenIndices bool) int {
        target := make([]int, 0, len(oddPos))
        for i := 0; i < N; i++ {
            if (i % 2 == 0) == oddAtEvenIndices {
                target = append(target, i)
            }  
        }
        // this pattern isn't count-compatible?
        if len(target) != len(oddPos) {
            return -1
        }

        total := 0
        for i := range oddPos {
            total += abs(oddPos[i] - target[i])
        }
        return total
    }

    if evenCount == oddCount {
		case1 := cost(true)  // odd numbers at even indices
		case2 := cost(false) // odd numbers at odd indices
		return min(case1, case2)
	}

    if oddCount > evenCount {
        // odd majority takes the majority (even) index slots
        return cost(true)
    }
    // even majority takes even index slots -> odds go to odd slots
    return cost(false)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}