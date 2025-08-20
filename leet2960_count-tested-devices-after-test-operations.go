func countTestedDevices(batteryPercentages []int) int {
    tested := 0

    for _, battery := range(batteryPercentages) {
        if battery > tested {
            tested++
        }
    }
    return tested
}