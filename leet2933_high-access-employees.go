func findHighAccessEmployees(access_times [][]string) []string {
    sort.Slice(access_times, func(i, j int) bool {
        if access_times[i][0] == access_times[j][0] {
            return access_times[i][1] < access_times[j][1]
        }
        return access_times[i][0] < access_times[j][0]
    })

    highAccess := make([]string, 0, 4)
    for i := 2; i < len(access_times); i++ {
        l := access_times[i - 2]
        r := access_times[i]

        if l[0] != r[0] {
            continue
        }

        if len(highAccess) > 0 && highAccess[len(highAccess) - 1] == l[0] {
            continue
        }

        if toMinutes(r[1]) - toMinutes(l[1]) < 60 {
            highAccess = append(highAccess, l[0])
        }
    }
    return highAccess
}

func toMinutes(s string) int {
    h, _ := strconv.Atoi(s[:2])
    m, _ := strconv.Atoi(s[2:])
    return h * 60 + m
}