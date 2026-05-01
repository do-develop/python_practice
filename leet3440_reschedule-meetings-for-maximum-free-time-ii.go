func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
    N := len(startTime)

    gaps := make([]int, N+1)
    gaps[0] = startTime[0]
    for i := 1; i < N; i++ {
        gaps[i] = startTime[i] - endTime[i-1]
    }
    gaps[N] = eventTime - endTime[N-1]

    // what's the largest gap BEFORE gap[i]?
    prefMax := make([]int, N+2)
    for i := 0; i < N+1; i++ {
        prefMax[i+1] = max(prefMax[i], gaps[i])
    }

    // what's the largest gap AFTER gap[i]
    sufMax := make([]int, N+2)
    for i := N; i >= 0; i-- {
        sufMax[i] = max(sufMax[i+1], gaps[i])
    }

    ans := 0

    for i := 0; i < N; i++ {
        duration := endTime[i] - startTime[i]
        maxOtherGap := max(prefMax[i], sufMax[i+2])
        mergedGap := gaps[i] + gaps[i+1]
        if maxOtherGap >= duration {
            ans = max(ans, mergedGap+duration)
        } else { // CANNOT relocate meeting i
            ans = max(ans, mergedGap)
        }
    }
    return ans
}