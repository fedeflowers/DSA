"""
```markdown
## Explanation of the Solution for "Reverse Linked List"

### 1. Approach
The solution provided uses an iterative method to reverse a singly linked list. The idea is to traverse the linked list while adjusting the `next` pointers of each node so that they point to the previous node instead of the next one.

- **Initialization**: Start with a `prev` pointer set to `None`. This will eventually become the new head of the reversed list.
- **Traversal**: A `while` loop is used to iterate through the list as long as `head` is not `None`.
  - Inside the loop:
    - Store the next node (`next = head.next`).
    - Reverse the current node's pointer (`head.next = prev`).
    - Move the `prev` pointer to the current node (`prev = head`).
    - Advance the `head` pointer to the next node (`head = next`).
- **Return**: After the loop ends, `prev` points to the new head of the reversed list, which is returned.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n) where n is the number of nodes in the linked list. This is because we traverse each node exactly once.
- **Space Complexity**: O(1). The algorithm uses a fixed amount of space for the `prev`, `head`, and `next` pointers, regardless of the size of the input list.

### 3. Efficiency of the Approach
This approach is efficient for several reasons:
- It operates in linear time, making it suitable even for large lists.
- It only uses a constant amount of additional space (O(1)), which is optimal compared to solutions that might use extra data structures (like arrays) to store values.
- The in-place modification of the list reduces memory overhead, providing a space-efficient solution that doesn't require additional allocations.

Overall, this iterative method is straightforward and effective for reversing a linked list, leveraging pointer manipulation to achieve the desired outcome.
```

Runtime: undefined
Memory: 20480000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev
