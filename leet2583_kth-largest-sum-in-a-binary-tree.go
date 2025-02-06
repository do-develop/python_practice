/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func kthLargestLevelSum(root *TreeNode, k int) int64 {
    levelSum := &MinHeap{}
    q := []*TreeNode{root}

    for len(q) > 0 {
        qsize := len(q)
        total := 0

        for range qsize {
            cur := q[0]
            q = q[1:]
            
            total += cur.Val
            if cur.Left != nil {
                q = append(q, cur.Left)
            }
            if cur.Right != nil {
                q = append(q, cur.Right)
            }
        }

        if levelSum.Len() < k {
            heap.Push(levelSum, total)
        } else if (*levelSum)[0] < total {
            heap.Pop(levelSum)
            heap.Push(levelSum, total)
        }
    }
    if levelSum.Len() < k {
        return -1
    }
    return int64((*levelSum)[0])
}

type MinHeap []int
func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}