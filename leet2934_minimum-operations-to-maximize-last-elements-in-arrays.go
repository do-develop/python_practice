func minOperations(nums1 []int, nums2 []int) int {
    case1 := helper(nums1, nums2)
    nums1[len(nums1) - 1], nums2[len(nums2) - 1] = nums2[len(nums2) - 1], nums1[len(nums1) - 1]
    case2 := 1 + helper(nums1, nums2)
    return min(case1, case2)
}

func helper(nums1 []int, nums2 []int) int {
    max1 := nums1[len(nums1) - 1]
    max2 := nums2[len(nums2) - 1]
    ops :=  0

    for i := 0; i < len(nums1) - 1; i++ {
        curr1 := nums1[i]
        curr2 := nums2[i]

        if curr1 <= max1 && curr2 <= max2 {
            continue
        }
        if curr1 <= max2 && curr2 <= max1 {
            ops++
            continue
        }
        return -1
    }
    return ops
}