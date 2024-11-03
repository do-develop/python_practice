/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 var ans int

 func amountOfTime(root *TreeNode, start int) int {
	 ans = 0
	 dfs(root, start)
	 return ans
 }
 
 func dfs(root *TreeNode, start int) (int, bool) {
	 if root == nil {
		 return 0, false
	 }
	 left, foundInLeft := dfs(root.Left, start)
	 right, foundInRight := dfs(root.Right, start)
 
	 if root.Val == start {
		 ans = max(ans, max(left, right))
		 return 1, true
	 }
 
	 if foundInLeft {
		 ans = max(ans, left + right)
		 return left + 1, true
	 } else if foundInRight {
		 ans = max(ans, left + right)
		 return right + 1, true
	 } else {
		 return max(left, right) + 1, false
	 }
 
 }
 
 func max(a, b int) int {
	 if a > b {
		 return a
	 }
	 return b
 }