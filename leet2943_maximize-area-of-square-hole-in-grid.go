func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
    h := maxHole(hBars)
    v := maxHole(vBars)

    if h > v {
        return v*v
    }
    return h*h
}


func maxHole(bars []int) int {
    sort.Ints(bars)
    var maxConsecutive, currCons int

    for i := 0; i < len(bars); i++ {
        if i > 0 && bars[i] == bars[i - 1] + 1 {
            currCons++
        } else {
            currCons = 1
        }

        if currCons > maxConsecutive {
            maxConsecutive = currCons
        }
    }
    return maxConsecutive + 1
}