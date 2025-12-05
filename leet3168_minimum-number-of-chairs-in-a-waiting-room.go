func minimumChairs(s string) int {
    chairs, count := 0, 0

    for _, status := range s {
        switch status {
            case 'E':
            count++
            case 'L':
            count--
        }

        if count > chairs {
            chairs = count
        }
    }
    return chairs
}