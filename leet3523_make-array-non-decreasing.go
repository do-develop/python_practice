func maximumPossibleSize(nums []int) int {
    size := 0
    prev := -1

    for _, num := range nums {
        if num >= prev {
            prev = num
            size++
        }
    }
    return size
}