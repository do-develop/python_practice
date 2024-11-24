func countTime(time string) int {
    // Brute-force approach
    res := 1

    // Hour
    if time[0] == '?' && time[1] == '?' {
        res *= 24
    } else if time[0] == '?' {
        if time[1] < '4' {
            res *= 3
        } else {
            res *= 2
        }
    } else if time[1] == '?' {
        if time[0] <= '1' {
            res *= 10
        } else {
            res *= 4
        }
    }

    // Minute
    if time[3] == '?' && time[4] == '?'{
        res *= 60
    } else if time[3] == '?' {
        res *= 6
    } else if time[4] == '?' {
        res *= 10
    }

    return res
}