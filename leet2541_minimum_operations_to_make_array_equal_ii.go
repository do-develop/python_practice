func minOperations(nums1 []int, nums2 []int, k int) int64 {
    if k == 0 {
        if reflect.DeepEqual(nums1, nums2) {
            return 0
        }
        return -1
    }

    var balance, ops int

    for i := 0; i < len(nums1); i++ {
        diff := nums1[i] - nums2[i]

        if diff % k != 0 {
            return -1
        }

        balance += diff

        if diff > 0 {
            ops += (diff / k)
        }
    }

    if balance == 0 {
        return int64(ops)
    }
    return -1
}