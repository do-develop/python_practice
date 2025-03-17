func matrixSum(nums [][]int) int {
    rows, cols := len(nums), len(nums[0])

    for r := 0; r < rows; r++ {
        sort.Slice(nums[r], func(i, j int) bool {
            return nums[r][i] > nums[r][j]
        })
    }

    total := 0
    for c := 0; c < cols; c++ {
        score := 0
        for r := 0; r < rows; r++ {
            if nums[r][c] > score {
                score = nums[r][c]
            }
        }
        total += score
    }
    return total
}