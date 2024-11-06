func garbageCollection(garbage []string, travel []int) int {
    prefix := make([]int, len(travel) + 1)

    for i:=1; i<len(prefix); i++ {
        prefix[i] = prefix[i - 1] + travel[i - 1]
    }

    lastP := 0
    lastG := 0
    lastM := 0
    collectionTime := 0
    travelTime := 0

    for i, gCollect := range(garbage) {
        if i != 0 {
            travelTime += travel[i - 1]
        }
        collectionTime += len(gCollect)
        for j := 0; j < len(gCollect); j++ {
            if gCollect[j] == 'M' {
                lastM = travelTime
            } else if gCollect[j] == 'P' {
                lastP = travelTime
            } else if gCollect[j] == 'G' {
                lastG = travelTime
            }
        }
    }

    return collectionTime + lastP + lastG + lastM
}