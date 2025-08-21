func getGoodIndices(variables [][]int, target int) []int {
    var result []int

    for i, row := range variables {
        a, b, c, m := row[0], row[1], row[2], row[3]
        if power(power(a, b, 10), c, m) == target {
            result = append(result, i)
        }
    }
    return result
}

func power(base, exp, mod int) int {
    result := 1
    for exp > 0 {
        if exp % 2 == 1{
            result = (result * base) % mod
        }
        base = (base * base) % mod
        exp /= 2
    }
    return result
}