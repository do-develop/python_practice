func beautifulSubarrays(nums []int) int64 {
    counter := make(map[int]int)
    counter[0] = 1 // prefix starts with a zero XOR

    answer, xor := 0, 0
    for _, num := range nums {
        xor ^= num
        answer += counter[xor] // if xor has been seen, there exists a subarray where xor is zero
        counter[xor] += 1
    }
    return int64(answer)
}