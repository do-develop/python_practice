func maxBalancedShipments(weight []int) int {
    prev, shipments := 0, 0

    for _, w := range weight {
        if w < prev {
            shipments++
            prev = 0
        } else {
            prev = w
        }
    }
    return shipments
}