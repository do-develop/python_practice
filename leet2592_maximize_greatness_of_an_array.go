func maximizeGreatness(nums []int) int {
    sort.Slice(nums, func(x, y int) bool {
        return nums[x] < nums[y]
    })

    var great int = 0
    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[great] {
            great++
        }
    }
    return great
}