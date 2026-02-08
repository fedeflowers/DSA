"""
## Explanation of the LeetCode Solution for "Balanced Binary Tree"

### 1. Approach Explanation

The solution defines a binary tree and checks whether it is balanced, meaning that for any node, the height of the left and right subtrees differs by at most one. The algorithm uses two helper functions: `height` and `balanced`.

- **Height Calculation**: The `height` function calculates the height of each subtree recursively. A tree is defined as balanced if:
  - The height of the left and right subtrees differ by at most 1.
  - Both subtrees are also balanced.

- **Storage of Heights**: The heights of the subtrees rooted at each node are stored in a dictionary called `heights`, where the key is the node and the value is the height of that node.

- **Balanced Check**: The `balanced` function checks whether each subtree meets the balance condition by:
  - Ensuring that the absolute difference between the heights of its left and right child is less than or equal to 1.
  - Recursively checking whether both the left and right subtrees are balanced.

Here's the workflow:
1. First, calculate the heights for all nodes using the `height` function.
2. Then, verify whether the tree is balanced using the `balanced` function.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: \(O(N)\)
  - Here, \(N\) is the number of nodes in the tree. Each node is visited once to calculate its height and once again to check if the tree is balanced.

- **Space Complexity**: \(O(N)\)
  - The space complexity arises from the storage of heights in a dictionary and the maximum depth of the recursion stack. In the worst case (where the tree is a skewed tree), the maximum height of the recursion will be \(O(N)\), and the height dictionary will also consume \(O(N)\).

### 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Single Pass for Height Calculation**: By calculating the height of each subtree and immediately storing it, the solution avoids recalculating heights multiple times. This reduces unnecessary duplicate work.

- **Separation of Concerns**: The two helper functions (`height` and `balanced`) clearly delineate between the tasks of computing heights and assessing balance. This modularity not only improves readability but also allows for easier debugging and enhancement.

- **Direct Access via Dictionary**: The use of a dictionary to store heights allows for \(O(1)\) average-time complexity when accessing the height of a node, leading to an overall efficient balance check.

Overall, the algorithm effectively uses recursion and a hash map to solve the balanced binary tree problem optimally, balancing both time and space complexities within acceptable limits.

Runtime: undefined
Memory: 21400000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heights = {None: 0}
        def height(root: TreeNode):
            if root is None:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            
            heights[root] = max(left, right) + 1
            return heights[root]

        def balanced(root):
            if root is None:
                return True

            return (abs(heights[root.left] - heights[root.right]) <= 1 and 
            balanced(root.left) and 
            balanced(root.right))

        height(root)
        return balanced(root)
        
