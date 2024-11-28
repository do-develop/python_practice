func haveConflict(event1 []string, event2 []string) bool {
    minEnd := min(getTime(event1[1]), getTime(event2[1]))
    maxStart := max(getTime(event1[0]), getTime(event2[0]))
    return minEnd >= maxStart 
}

func getTime(event string) int {
    hours := int(event[0]-'0')*10 + int(event[1]-'0')
    minutes := int(event[3]-'0')*10 + int(event[4]-'0')
    return hours * 60 + minutes
}