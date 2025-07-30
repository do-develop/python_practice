func findChampion(n int, edges [][]int) int {
    isUndefeated := make([]bool, n)
    for i := range isUndefeated {
        isUndefeated[i] = true
    }

    for _, edge := range edges {
        _, loser := edge[0], edge[1]
        isUndefeated[loser] = false
    }

    champion := -1
    champCount := 0

    for team := 0; team < n; team++ {
        if isUndefeated[team] {
            champion = team
            champCount++
        } 
    }

    if champCount == 1 {
        return champion
    }
    return -1
}