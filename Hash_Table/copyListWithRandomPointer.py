"""
```markdown
## Explanation of "Copy List with Random Pointer" Solution

### 1. Approach Explanation

The solution involves a three-pass method to create a deep copy of a linked list where each node has a `next` pointer and a `random` pointer. 

**Step 1: Copy Next Nodes**
- Traverse the original list and create a copy of each node.
- For each node in the original list, a new node is created and inserted right next to it. The `next` pointer of the original node is updated to point to its copy, effectively forming a modified list where each original node is followed by its copy.

**Step 2: Copy Random Pointers**
- In this step, we leverage the newly created nodes. For each original node, we set the `random` pointer of its copy node to point to the copy of the random node of the original node. Since the copies are interleaved within the original list, we can easily access the copy of any random node using the `next` pointer.

**Step 3: Separate the Two Lists**
- Finally, we restore the original list to its initial state and extract the copied nodes into a separate list. We traverse through the altered list and update the `next` pointers of the copied nodes to jump over the original nodes.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** O(N)
  - We traverse the list three times:
    - Once to create the copies of nodes.
    - Once to assign the random pointers.
    - Once to separate the copied nodes from the original list.
  
  Thus, the total time complexity is O(N), where N is the number of nodes in the linked list.

- **Space Complexity:** O(1)
  - The algorithm only uses a fixed amount of space for temporary pointers (like `curr`, `next_node`, etc.). The space occupied by the new nodes does not count towards space complexity as they are integral to the output.

### 3. Why This Approach is Efficient

This approach leverages the properties of linked lists effectively with only three passes through the list. Instead of using a hash map to keep track of original and copied node relationships (which would have increased space complexity), it interleaves the copy nodes with the original nodes. This avoids the extra space overhead while enabling efficient traversal.

Maintaining a linear pass for random pointer copying ensures that the index of the copied nodes is directly accessible through their positioning in the modified list. Ultimately, this results in a clean and efficient solution to the problem of deep copying a complex linked list structure.
```

Runtime: undefined
Memory: 20112000
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # copy next node
        curr = head
        while curr:
            next_node = Node(curr.val, curr.next)
            curr.next = next_node
            curr = next_node.next

        # copy random pointer
        curr = head
        while curr: 
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # get only copy nodes
        curr = head
        copy_head = head.next
        while curr:
            copy_node = curr.next
            next_pointer = copy_node.next
            if next_pointer:
                copy_node.next = next_pointer.next
            curr = next_pointer

        return copy_head


