func addMinimum(word string) int {
    add, target := 0, 0
    var pos int

    for _, c := range word {
        pos = int(c - 'a')
        for pos != target {
            target = (target + 1) % 3
            add++
        }
        target = (target + 1) % 3
    }

    if target > 0 {
        add += 3 - target
    }
    return add

}
