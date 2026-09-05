func earliestTime(tasks [][]int) int {
    mini := tasks[0][0] + tasks[0][1]

    for _, task := range tasks {
        if mini > task[0] + task[1] {
            mini = task[0] + task[1]
        }
    }    
    return mini
}