func returnToBoundaryCount(nums []int) int {
    curr, count := 0, 0

    for _, num := range nums {
        curr += num
        if curr == 0 {
            count++
        }
    }
    return count
}