var emptyCells [][2]int
var stoneCells [][2]int

func minimumMoves(grid [][]int) int {
   emptyCells = [][2]int{}
   stoneCells = [][2]int{}

   for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if grid[i][j] == 0 {
                emptyCells = append(emptyCells, [2]int{i, j})
            } else if grid[i][j] > 1 {
                stoneCells = append(stoneCells, [2]int{i, j})
            }
        }
   } 
   return solve(grid, 0)
}

func solve(grid[][]int, emptyCellIdx int) int {
    // base case
    if emptyCellIdx == len(emptyCells) { return 0 }
    receiver := emptyCells[emptyCellIdx]
    ans := math.MaxInt
    for i := 0; i < len(stoneCells); i++ {
        giver := stoneCells[i]
        if grid[giver[0]][giver[1]] == 1 { continue }
        distance := abs(receiver[0] - giver[0]) + abs(receiver[1] - giver[1])
        // account for taking this stone
        grid[giver[0]][giver[1]]--
        res := distance + solve(grid, emptyCellIdx + 1)
        // backtrack
        grid[giver[0]][giver[1]]++
        ans = min(res, ans)
    }
    return ans
}

func min(x, y int) int { if x < y { return x }; return y }
func abs(x int) int { if x < 0 { return -x }; return x }