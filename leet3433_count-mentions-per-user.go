func countMentions(numberOfUsers int, events [][]string) []int {
    mentions := make([]int, numberOfUsers)
    onlineAt := make([]int, numberOfUsers)

    sort.SliceStable(events, func(i, j int) bool {
        ti, _ := strconv.Atoi(events[i][1])
        tj, _ := strconv.Atoi(events[j][1])
        if ti != tj {
            return ti < tj
        }
        // offline is processed first
        if events[i][0] == "OFFLINE" && events[j][0] == "MESSAGE" {
            return true
        }
        return false
    })

    for _, event := range events {
        eventType := event[0]
        timestamp, _ := strconv.Atoi(event[1])
        payload := event[2]

        if eventType == "OFFLINE" {
            uid, _ := strconv.Atoi(payload)
            onlineAt[uid] = timestamp + 60
        } else {
            switch payload {
            case "ALL":
                for i := range mentions {
                    mentions[i]++
                }
            case "HERE":
                for i := 0; i < numberOfUsers; i++ {
                    if onlineAt[i] <= timestamp {
                        mentions[i]++
                    }
                }
            default:
                for _, token := range strings.Fields(payload) {
                    uid, _ := strconv.Atoi(strings.TrimPrefix(token, "id"))
                    mentions[uid]++
                }
            }
        }
    }
    return mentions
}