func maxCount(banned []int, n int, maxSum int) int {
    isBanned := make(map[int]bool)

    for _, v := range(banned) {
        isBanned[v] = true
    }

    num := 1
    count, total := 0, 0
    for num <= n {
        if (total + num <= maxSum && !isBanned[num]){
            count++
            total += num
        }
        num++
    }
    return count
}