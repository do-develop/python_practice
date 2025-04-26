efunc minimumIndex(nums []int) int {
    N := len(nums)
    count1 := make(map[int]int)
    count2 := make(map[int]int)

    for i := 0; i < N; i++ {
        count2[nums[i]]++
    }

    for idx := range nums {
        num := nums[idx]
        count1[num]++
        count2[num]--

        val1, _ := count1[num]
        val2, _ := count2[num]

        if val1 * 2 > idx + 1 && val2 * 2 > N - idx - 1 {
            return idx
        }
    }
    return -1
}