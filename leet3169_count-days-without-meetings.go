func countDays(days int, meetings [][]int) int {
    N := len(meetings)

    if N == 0 {
        return days
    }

    sort.Slice(meetings, func(x, y int) bool {
        return meetings[x][0] < meetings[y][0]
    })
    l, r := meetings[0][0], meetings[0][1]

    for i := 0; i < N; i++ {
        if r >= meetings[i][0] {
            r = max(r, meetings[i][1])
        } else {
            days -= r - l + 1
            l, r = meetings[i][0], meetings[i][1]
        }
    }

    return days - (r - l + 1)
}