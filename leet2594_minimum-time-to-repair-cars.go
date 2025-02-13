func repairCars(ranks []int, cars int) int64 {
    count := make(map[int]int) // count occurence of rank
    for _, rank := range(ranks) {
        count[rank]++
    }

    sortedRanks := make([]int, 0, len(count))
    for key := range count {
        sortedRanks = append(sortedRanks, int(key))
    }
    sort.Ints(sortedRanks)

    left, right := 1, sortedRanks[len(sortedRanks) - 1] * cars * cars
    for left < right {
        mid := (left + right) / 2
        sum := 0
        for _, rank := range sortedRanks {
            sum += int(math.Sqrt(float64(mid/rank))) * count[rank]
        }

        if sum < cars {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return int64(left)
}

