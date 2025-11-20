# Problem: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next