/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func reverseOddLevels(root *TreeNode) *TreeNode {
    dfs(root.Left, root.Right, 1)
    return root
}

func dfs(l *TreeNode, r *TreeNode, level int) {
    if l == nil || r == nil {
        return
    }

    if level % 2 == 1 {
        l.Val, r.Val = r.Val, l.Val
    }

    dfs(l.Left, r.Right, level + 1) // outer-part swap
    dfs(l.Right, r.Left, level + 1) // inner-part swap
}