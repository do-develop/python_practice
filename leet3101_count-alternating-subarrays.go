func countAlternatingSubarrays(nums []int) int64 {
    countSub := 1
    lastSubSize := 1

    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i - 1] {
            lastSubSize++
        } else {
            lastSubSize = 1
        }
        countSub += lastSubSize
    }

    return int64(countSub)
}