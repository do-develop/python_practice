func sumCounts(nums []int) int {
    var counter int

    for i := range nums {
        set := [101]bool{} // using contraints
        distinct := 0

        for j := i; j < len(nums); j++ {
            if !set[nums[j]] {
                set[nums[j]] = true
                distinct++
            }
            counter += distinct * distinct        
        }
    }
    return counter
}