func evenNumberBitwiseORs(nums []int) int {
    bitor := 0

    for _, n := range nums {
        if n % 2 == 0 {
            bitor |= n
        }
    }
    return bitor
}