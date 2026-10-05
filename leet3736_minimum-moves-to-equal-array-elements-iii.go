func minMoves(nums []int) int {
    maxi := slices.Max(nums)
    moves := 0

    for _, num := range nums {
        moves += (maxi - num)
    }

    return moves
}