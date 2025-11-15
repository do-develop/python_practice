func minimumAddedInteger(nums1 []int, nums2 []int) int {
    sort.Ints(nums1)
    sort.Ints(nums2)

    for i := 2; i > 0 ; i-- {
        skip := i

        for j := i + 1; skip < 3 && j - skip < len(nums2); j++ {
            if nums2[j - skip] - nums1[j] != nums2[0] - nums1[i] {
                skip++
            }
        }

        if skip < 3 {
            return nums2[0] - nums1[i]
        }
    }

    return nums2[0] - nums1[0]
}