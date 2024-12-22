/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func closestNodes(root *TreeNode, queries []int) [][]int {
    var res [][]int
    var arr []int

    makeArray(root, &arr)

    for _, num := range queries {
        l, r := 0, len(arr) - 1
        if num < arr[l] {
            res = append(res, []int{-1, arr[l]})
            continue
        }

        if num > arr[r] {
            res = append(res, []int{arr[r], -1})
            continue
        }

        found := false
        for l <= r {
            mid := (l + r) / 2
            if num == arr[mid] {
                found = true
                res = append(res, []int{num, num})
                break
            }
            if num > arr[mid] {
                l = mid + 1
            } else {
                r =  mid - 1
            }
        }
        if !found {
            res = append(res, []int{arr[l-1], arr[r+1]})
        }
    }
    return res
}

func makeArray(root *TreeNode, arr *[]int){
    if root == nil {
        return
    }

    makeArray(root.Left, arr)
    *arr = append(*arr, root.Val)
    makeArray(root.Right, arr)
}