func maxFreeTime(eventTime int, k int, startTime []int, endTime []int) int {
    N := len(startTime)
    res := 0
    sum := make([]int, N + 1)

    for i := 0; i < N; i++ {
        sum[i+1] = sum[i] + endTime[i] - startTime[i]
    }

    for i := k-1; i < N; i++ {
        var right int
        if i == N-1 {
            right = eventTime
        } else {
            right = startTime[i + 1]
        }
        var left int
        if i == k-1 {
            left = 0
        } else {
            left = endTime[i - k]
        }
        // 구간 전체 길이 - (이 구간 안 이벤트들의 총 길이)
        res = max(res, right-left - (sum[i+1]-sum[i+1-k]))
    }
    return res
}