"""
## Explanation of the Solution for "Balanced Binary Tree"

### 1. Brief Explanation of the Approach
The problem requires checking whether a binary tree is height-balanced, which means that for any node in the tree, the height difference between its left and right subtrees should not exceed 1.

The solution uses a recursive helper function `check`, which computes the height of the tree while simultaneously checking for balance:
- If a node is `None`, it returns a height of `0`.
- It recursively calls itself for the left and right children of the current node.
- If, during the recursion:
  - The height of the left subtree is found to be `-1` (indicating an imbalance), it propagates this `-1` back up.
  - Similarly for the right subtree.
- After determining the heights of both subtrees, it checks the balance condition. If the height difference is greater than `1`, it returns `-1` to indicate that the tree is not balanced at that node.
- If the node is balanced, it returns its height.

Finally, the balance check is completed by seeing if the initial call to `check(root)` returns `-1` (indicating imbalance) or a valid height.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity is O(N), where N is the number of nodes in the binary tree. This is because each node is visited exactly once during the height calculation.
  
- **Space Complexity**: The space complexity is O(H), where H is the height of the tree. This space is used by the call stack due to the recursion. In the worst case (for a skewed tree), this could be O(N), but in a balanced tree, it would be O(log N).

### 3. Why This Approach is Efficient
This approach is efficient due to its combination of height calculation and balance checking in a single traversal of the tree, rather than requiring separate passes. By avoiding the need to store and subsequently recompute heights for left and right subtrees during a second traversal, the method minimizes redundant computations. This results in linear time complexity with respect to the number of nodes in the tree. Thus, it optimally determines both height and balance status in one go.

Runtime: undefined
Memory: 20520000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         heights = {None: 0}
#         def height(root: TreeNode):
#             if root is None:
#                 return 0
            
#             left = height(root.left)
#             right = height(root.right)
            
#             heights[root] = max(left, right) + 1
#             return heights[root]

#         def balanced(root):
#             if root is None:
#                 return True

#             return (abs(heights[root.left] - heights[root.right]) <= 1 and 
#             balanced(root.left) and 
#             balanced(root.right))

#         height(root)
#         return balanced(root)
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            if left == -1: return -1  # Propagate imbalance
            
            right = check(node.right)
            if right == -1: return -1 # Propagate imbalance
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1

        return check(root) != -1
