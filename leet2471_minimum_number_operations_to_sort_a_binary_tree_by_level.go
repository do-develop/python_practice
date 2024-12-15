/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func minimumOperations(root *TreeNode) int {
    // BFS to traverse by level
    result, queue := 0, []*TreeNode{root}
    for len(queue) > 0 {
        size, nums := len(queue), make([]int, 0)
        for i := 0; i < size; i++ {
            node := queue[0]
            queue = queue[1:]
            nums = append(nums, node.Val)
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        result += countMinOperations(nums)
    }
    return result
}

func countMinOperations(nums []int) int {
    sorted := make([]int, len(nums))
    copy(sorted, nums)
    sort.Ints(sorted)
    index := make(map[int]int)
    for i, num := range nums {
        index[num] = i
    }

    operations := 0
    for i, num := range nums {
        if num != sorted[i] {
            operations++
            newPos := index[sorted[i]]
            index[nums[i]] = newPos
            index[nums[newPos]] = i
            nums[i], nums[newPos] = nums[newPos], nums[i]
        }
    }
    return operations
}