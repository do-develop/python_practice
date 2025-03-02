func rowAndMaximumOnes(mat [][]int) []int {
    output := []int{0,0}
    for idx, item := range mat {
        counter := 0
        for _, v := range item {
            if v == 1 {
                counter++
            }
        }
        if counter > output[1] {
            output[0] = idx
            output[1] = counter
        }
    }
    return output
}
