func hardestWorker(n int, logs [][]int) int {
    workerId := logs[0][0]
    longest := logs[0][1]

    for i := 1; i < len(logs); i++ {
        time := logs[i][1] - logs[i-1][1]
        if time > longest {
            longest = time
            workerId = logs[i][0]
        } else if time == longest && logs[i][0] < workerId {
            workerId = logs[i][0]
        }
    }
    return workerId
}