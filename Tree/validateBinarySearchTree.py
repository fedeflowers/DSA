"""
```markdown
# Explanation of the LeetCode Solution for "Validate Binary Search Tree"

## 1. Brief Explanation of the Approach

The provided solution employs a recursive approach to validate if a binary tree is a binary search tree (BST). The validation process uses a helper function `validate(node, low, high)` that checks whether the value of the current node lies within a specified range defined by `low` and `high`.

- **Base Case**: If the current `node` is `None`, it is considered a valid subtree; therefore, the function returns `True`.
- **Value Check**: The function checks if the current `node.val` is strictly between `low` and `high`. If it is not, the function returns `False`, indicating that the binary tree cannot be a BST.
- **Recursive Calls**: The function then recursively checks the left and right children:
  - The left child must have values less than the current node's value, so it updates the range to `(low, node.val)`.
  - The right child must have values greater than the current node's value, so it updates the range to `(node.val, high)`.
- The overall result is a conjunction of the validity of the left and right subtrees.

The recursion is initiated with the entire range of possible values for a binary search tree: from negative infinity to positive infinity.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. This is because each node is visited exactly once in a depth-first traversal.
  
- **Space Complexity**: The space complexity is O(H), where H is the height of the binary tree. This accounts for the space required by the recursive function call stack. In the worst-case scenario (for a skewed tree), H could be O(N). However, for a balanced tree, H would be O(log N).

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Direct Validation**: It directly checks the properties of a BST during the traversal, ensuring that the values are within the valid ranges without needing to perform multiple passes or re-evaluations of the nodes.
- **Recursive Depth-First Search**: The use of recursion allows the function to naturally explore the depths of the tree, effectively handling each branch independently.
- **Constant Range Check**: By maintaining bounds on the values for each node's left and right children, the algorithm avoids cumbersome data structures or additional space that would be needed to store the entire tree or its nodes.
- **Early Exit**: The function can exit early if it encounters any invalid conditions, providing potentially faster validation in practice depending on the structure of the tree.

Overall, the implemented solution is both simple and efficient, leveraging the properties of binary search trees and recursion effectively.
```

Runtime: undefined
Memory: 18648000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            
            # Current node must be strictly between low and high
            if not (low < node.val < high):
                return False
            
            # Left child: must be < current node.val
            # Right child: must be > current node.val
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))
