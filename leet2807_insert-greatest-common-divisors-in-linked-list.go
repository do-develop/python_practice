/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    curr := head

    for curr != nil && curr.Next != nil {
        gcdVal := gcd(curr.Val, curr.Next.Val)
        newNode := &ListNode{Val: gcdVal}

        // insert the new node between
        newNode.Next = curr.Next
        curr.Next = newNode

        // move to the next pair of node
        curr = newNode.Next
    }
    return head
}

func gcd(x, y int) int {
    if y == 0 {
        return x
    }
    return gcd(y, x % y)
}