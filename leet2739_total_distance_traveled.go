func distanceTraveled(mainTank int, additionalTank int) int {
    usuable := 0

    for mainTank >= 5 {
        mainTank -= 5
        usuable += 5

        if additionalTank != 0 {
            additionalTank--
            mainTank++
        }
    }
    return (usuable + mainTank) * 10
}