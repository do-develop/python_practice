/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
    ans := head

    if head.Val >= 5 {
        head = &ListNode{Val: 1, Next: head}
        ans = head
        head = head.Next
    }

    for head != nil && head.Next != nil {
        if head.Next.Val < 5 {
            head.Val = (head.Val * 2) % 10
        } else {
            head.Val = (head.Val * 2 + 1) % 10
        }
        head = head.Next
    }

    head.Val = (head.Val * 2) % 10
    return ans
}