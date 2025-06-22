func maximumSumOfHeights(heights []int) int64 {
    mxSum := 0
    for i := range heights {
        mxSum = max(getTowerSum(i, heights), mxSum)
    }
    return int64(mxSum)
}

func getTowerSum(peakIdx int, heights []int) int {
    heightsSum := heights[peakIdx]

    // right
    lowest := heights[peakIdx]
    for i := peakIdx + 1; i < len(heights); i++ {
        heightsSum += heights[i]

        if lowest > heights[i] {
            lowest = heights[i]
        } else if heights[i] > lowest {
            heightsSum -= heights[i] - lowest
        }
    }

    // left 
    lowest = heights[peakIdx]
    for i := peakIdx - 1; i >= 0; i-- {
        heightsSum += heights[i]

        if lowest > heights[i] {
            lowest = heights[i]
        } else if heights[i] > lowest {
            heightsSum -= heights[i] - lowest
        }
    }
    return heightsSum
}