func maxBottlesDrunk(numBottles int, numExchange int) int {
    full := numBottles
    empty, drunk := 0, 0
    currExchange := numExchange

    for full > 0 {
        drunk += full
        empty += full
        full = 0

        for empty >= currExchange {
            empty -= currExchange
            full++
            currExchange++
        }
    }
    return drunk
}