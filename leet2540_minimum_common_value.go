func getCommon(nums1 []int, nums2 []int) int {
    first, second := 0, 0

    for first < len(nums1) && second < len(nums2) {
        if nums1[first] < nums2[second] {
            first++
        } else if nums1[first] > nums2[second] {
            second++
        } else {
            return nums1[first]
        }
    }
    return -1
}