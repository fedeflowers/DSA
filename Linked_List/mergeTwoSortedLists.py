"""
```markdown
## Explanation of the "Merge Two Sorted Lists" Solution

### 1. Approach

The provided solution merges two sorted linked lists (`list1` and `list2`) into a single sorted linked list. The process is done iteratively by maintaining a pointer (`curr`) that traverses and constructs the new merged list. Here’s a step-by-step breakdown:

- **Initialization**: A dummy node (`dummy`) is created to serve as the starting point of the merged list. A pointer (`curr`) is initialized to point to this dummy node.

- **Merging Process**: The algorithm iterates while both `list1` and `list2` are not `None`:
  - If the value of the current node in `list1` is smaller than that in `list2`, the current node of `list1` is appended to the merged list, and `list1` is moved to its next node.
  - Otherwise, the current node of `list2` is appended to the merged list, and `list2` is similarly advanced.

- **Remaining Nodes**: Once one of the lists is exhausted, the remaining nodes of the other list (if any) are connected to the end of the merged list.

- **Return Statement**: The function returns `dummy.next`, which is the actual head of the newly formed merged list, skipping the dummy node.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N + M), where N is the length of `list1` and M is the length of `list2`. In the worst case, each node from both lists is processed exactly once.

- **Space Complexity**: O(1), as we are using a constant amount of extra space (the dummy node and a pointer) to assist in the merging process. The merged list is formed in place without the need for any additional data structures.

### 3. Efficiency of the Approach

This approach is efficient because:
- It processes each element from `list1` and `list2` exactly once, ensuring that the time complexity is linear relative to the total number of elements.
- The use of a dummy node simplifies the code, avoiding special cases for the head of the merged list, and it does not require any additional space for intermediate storage of nodes.
- This solution is optimal for merging two linked lists that are already sorted, leveraging their sorted properties for an efficient merge rather than needing to sort again.

Overall, the solution cleanly integrates the linked lists while adhering to the constraints of time and space performance.
```

Runtime: undefined
Memory: 17296000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        #connect remainings
        curr.next = list1 if list1 else list2

        return dummy.next
