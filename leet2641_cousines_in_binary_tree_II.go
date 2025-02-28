/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func replaceValueInTree(root *TreeNode) *TreeNode {
    q := []*TreeNode {root}
    root.Val = 0

    for len(q) > 0 {
        size := len(q)
        sum := 0

        for i := range size {
            curr := q[i]
            if curr.Left != nil {
                sum += curr.Left.Val
            }
            if curr.Right != nil {
                sum += curr.Right.Val
            }
        }

        for i := range size {
            curr := q[i]
            left, right := 0, 0
            if curr.Left != nil {
                left = curr.Left.Val
            }
            if curr.Right != nil {
                right = curr.Right.Val
            }
            if curr.Left != nil {
                curr.Left.Val = sum - left - right
                q = append(q, curr.Left)
            }
            if curr.Right != nil {
                curr.Right.Val = sum - left - right
                q = append(q, curr.Right)
            }
        }
        q = q[size:]
    }
    return root
}
