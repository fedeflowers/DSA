"""
## Balance a Binary Search Tree - Explanation of the Solution

### 1. Brief Explanation of the Approach
The solution takes a two-step approach to balance a binary search tree (BST):

1. **In-Order Traversal**: The first step is to traverse the given BST in an in-order fashion and collect all the node values into a list. This ensures that the values in the list are sorted because of the properties of a binary search tree.

2. **Building a Balanced BST**: The second step utilizes the sorted list of node values to construct a balanced BST. This is done recursively by taking the middle element of the list as the root (which helps in ensuring the balance) and making recursive calls to the left and right halves of the list to construct the left and right subtrees.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The in-order traversal takes O(N) time, where N is the number of nodes in the BST, to visit all nodes and store their values in the list.
  - The balanced BST construction also takes O(N) time, as we make a constant number of operations (finding the mid and creating nodes) for each of the N nodes.
  - Therefore, the overall time complexity of the solution is O(N).

- **Space Complexity**: 
  - We use O(N) space to store the node values in the list. Additionally, the recursive function calls will use space on the call stack, which in the worst case (for a skewed tree) can go up to O(N). However, since we are storing node values in a separate list, the dominant factor in space complexity is the list itself.
  - Thus, the overall space complexity is O(N).

### 3. Why This Approach is Efficient
This approach is efficient for several reasons:

- **Utilization of In-order Traversal**: In-order traversal captures the sorted order of nodes directly from a BST, which is a natural choice for creating a balanced BST from sorted data. This guarantees that the constructed tree maintains the properties of a BST.

- **Balanced Tree Construction**: By always selecting the middle element as the root during construction, the algorithm ensures that the tree remains balanced. This minimizes the height of the tree, thereby optimizing operations such as look-up, insertion, and deletion in future operations.

- **Clear and Concise Logic**: The two-step approach is straightforward to understand and implement, making the code maintainable and easier to reason about as compared to more complex tree manipulation algorithms.

Overall, this approach provides an efficient and clear method for balancing a binary search tree, making good use of sorted data and recursive tree construction techniques.

Runtime: N/A
Memory: N/A
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #explore all nodes and recreate tree: Brute force
        nodes = []
        def explore(root:TreeNode):
            if not root:
                return 

            explore(root.left)
            nodes.append(root.val)
            explore(root.right)

        explore(root)

        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nodes[mid])
            
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            
            return node
            
        return build(0, len(nodes) - 1)
