"""
```markdown
## Explanation of the Solution for "Validate Binary Search Tree"

### 1. A brief explanation of the approach
The solution uses a recursive helper function `validate` to check if a binary tree satisfies the properties of a binary search tree (BST). The key properties of a BST are:
- The left subtree of any node contains only nodes with values less than the node's value.
- The right subtree of any node contains only nodes with values greater than the node's value.
- Both the left and right subtrees must also be binary search trees.

The `validate` function takes three parameters: 
- `root`: the current node being validated,
- `low`: the lower bound for the node's value (inclusive),
- `high`: the upper bound for the node's value (exclusive).

The function works as follows:
1. If the current node (`root`) is `None`, it returns `True` because an empty tree is a valid BST.
2. It checks if the current node's value (`root.val`) is within the bounds defined by `low` and `high`. If it isn't, it returns `False`.
3. It recursively checks the left subtree, updating the upper bound to the current node's value, and the right subtree, updating the lower bound to the current node's value.
4. The function ultimately returns `True` if all nodes satisfy the BST properties, or `False` if any do not.

The process starts by invoking the `validate` function with the initial bounds of negative infinity and positive infinity.

### 2. Time and Space Complexity analysis
- **Time Complexity**: O(N)
  - Each node in the tree is visited exactly once, where N is the number of nodes in the tree.
- **Space Complexity**: O(H)
  - The space complexity is determined by the recursion stack. In the worst case (for a skewed tree), the depth of the recursion can be O(N), but for a balanced tree, it will be O(log N).

### 3. Why this approach is efficient
This approach is efficient due to its simplicity and directness in checking the BST properties. The use of bounds for each node ensures that:
- The correctness of the BST condition is verified at every level of recursion.
- Only essential nodes are checked against their respective bounds, avoiding unnecessary checks.
By enforcing the constraints of valid BST values through the traversal, the algorithm efficiently narrows down the validity checks without the need for additional data structures or traversals.

The recursive depth-first search (DFS) naturally fits the problem, capitalizing on the properties of trees and thereby keeping the implementation clean and easy to understand.
```

Runtime: undefined
Memory: 18656000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, low, high):
            if not root:
                return True

            if not (low < root.val < high):
                return False

            return (validate(root.left, low, root.val) and
                    validate(root.right, root.val, high))

        return validate(root, -float("inf"), float("inf"))
