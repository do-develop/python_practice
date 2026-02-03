func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
    N := len(energyDrinkA)

    var dpA []int64
    var dpB []int64

    dpA = append(dpA, int64(energyDrinkA[0]))
    dpB = append(dpB, int64(energyDrinkB[0]))

    for i := 1; i < N; i++ {
        dpA = append(dpA, int64(energyDrinkA[i]) + dpA[i-1])
        dpB = append(dpB, int64(energyDrinkB[i]) + dpB[i-1])
    }

    for i := 2; i < N; i++ {
        dpA[i] = max(dpA[i-1], dpB[i-2]) + int64(energyDrinkA[i])
        dpB[i] = max(dpB[i-1], dpA[i-2]) + int64(energyDrinkB[i])
    }
    return max(dpA[N-1], dpB[N-1])
}