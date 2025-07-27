func minSum(nums1 []int, nums2 []int) int64 {
    count1, count2 := 0, 0
    var sum1, sum2 int64

    for _, v := range nums1 {
        if v == 0 {
            count1++
        } else {
            sum1 += int64(v)
        }
    }

    for _, v := range nums2 {
        if v == 0 {
            count2++
        } else {
            sum2 += int64(v)
        }
    }

    if count1 == 0 && sum1 < sum2 + int64(count2) {
        return -1 
    }

    if count2 == 0 && sum2 < sum1 + int64(count1) {
        return -1
    }

    if sum1 + int64(count1) > sum2 + int64(count2) {
        return sum1 + int64(count1)
    }
    return sum2 + int64(count2)
}