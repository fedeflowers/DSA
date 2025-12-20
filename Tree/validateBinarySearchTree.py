"""
```markdown
## Explanation of the LeetCode Solution for "Validate Binary Search Tree"

### 1. Brief Explanation of the Approach
The solution employs a recursive helper function `valid` to verify if the given binary tree satisfies the properties of a binary search tree (BST). The key properties of a BST are:

- Each node's value must be greater than all values in its left subtree.
- Each node's value must be less than all values in its right subtree.

To enforce these properties during the validation process, the algorithm makes use of two parameters: `low` and `high`, which represent the acceptable range of values for each node in the tree. Initially, the range for the root node is set to `(-∞, ∞)`.

The steps in the `valid` function are as follows:

1. If the current node (`root`) is `None`, it returns `True`, indicating that an empty subtree is valid.
2. It checks if the current node's value (`root.val`) lies within the provided range (`low` < `root.val` < `high`). If it doesn't, it returns `False`, indicating a violation of the BST properties.
3. The function recursively checks the left and right subtrees, updating the value ranges accordingly:
   - For the left subtree, the updated range becomes `low` to `root.val`.
   - For the right subtree, the updated range becomes `root.val` to `high`.
4. The overall result is the logical AND of the results from both subtrees.

The initial call to `valid` is made with the root of the tree and the range `(-∞, ∞)`.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once, hence the linear time complexity.
  
- **Space Complexity**: O(H), where H is the height of the binary tree. This space is used for the recursion stack. In the case of a balanced tree, H will be O(log N); in the worst case (a skewed tree), H can be O(N).

### 3. Why this Approach is Efficient
This approach is efficient because:
- It directly leverages the properties of a binary search tree to determine the validity of the tree structure in a single traversal (depth-first search).
- It avoids unnecessary checks by managing the permissible value ranges dynamically with each recursive call.
- The recursive method is intuitive and straightforward, making it easy to implement and understand. The decision to return early for invalid cases also helps in reducing the number of function calls and checks.

Overall, this strategy effectively captures the requirements of the problem while maintaining optimal performance.
```

Runtime: undefined
Memory: 18604000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low, high):
            if not root:
                return True

            if not (low < root.val < high):
                return False

            return valid(root.left, low, root.val) and valid(root.right, root.val, high)

        return valid(root, -float("inf"), float("inf"))
