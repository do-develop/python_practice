func maximumSetSize(nums1 []int, nums2 []int) int {
    N := len(nums1)
    set1 := make(map[int]bool, N)
    set2 := make(map[int]bool, N)

    for i := 0; i < N; i++ {
        set1[nums1[i]] = true
        set2[nums2[i]] = true
    }

    half := N / 2

    for num := range set1 {
        if len(set1) <= half {
            break
        }
        if set2[num] {
            delete(set1, num)
        }
    }

    for num := range set1 {
        if len(set1) > half {
            delete(set1, num)
        } else {
            break
        }
    }

    ans := len(set1)
    count := 0

    for num := range set2 {
        if !set1[num] && count < half {
            ans++
            count++
        }
    }
    return ans
}