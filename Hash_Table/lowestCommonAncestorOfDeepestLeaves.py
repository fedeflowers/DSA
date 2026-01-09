"""
```markdown
## Explanation of the Solution

This solution aims to find the Lowest Common Ancestor (LCA) of the deepest leaves in a binary tree. The approach uses depth-first search (DFS) to traverse the tree while calculating the depth of each subtree and identifying the deepest leaves' common ancestor. 

### 1. Approach Explanation

- The function `lcaDeepestLeaves` is implemented within the `Solution` class. It takes the root of the binary tree as its input and returns the lowest common ancestor of the deepest leaves.
- A helper function `dfs` is defined which performs a recursive depth-first search on the tree. It returns a list containing two elements:
  - The first element is the depth of the deepest leaf found in the current subtree.
  - The second element is the TreeNode corresponding to the lowest common ancestor of the deepest leaves in that subtree.
- The base case for the recursion checks if the current node is null (`if not root:`). If it is null, it returns `[0, None]`, indicating a depth of 0 and no ancestor.
- When both the left and right children exist, it compares their depths:
  - If the left depth is greater, it returns the left depth plus one, along with the left ancestor.
  - If the right depth is greater, it returns the right depth plus one, along with the right ancestor.
  - If both depths are equal, it indicates that the current node is the ancestor of the deepest leaves, returning its depth plus one and the current node itself.
- Finally, `dfs(root)[1]` retrieves the lowest common ancestor from the result of the DFS traversal.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once during the DFS traversal.
- **Space Complexity**: O(H), where H is the height of the tree. This is due to the recursion stack. In the worst case (for example, in a skewed tree), H can be O(N), but for a balanced tree, it would be O(log N).

### 3. Efficiency of the Approach

- The proposed DFS approach is efficient because it combines the depth measurement and ancestor tracking in a single traversal, avoiding redundant computations.
- By returning information about both the depth and the potential ancestor in the same recursive call, the solution minimizes the number of traversals, leading to linear time complexity.
- This efficiency is particularly advantageous in large trees where multiple traversals would be computationally expensive.

Overall, this approach neatly encapsulates both the depth-first traversal and the logic for finding the common ancestor in one function, making it an elegant and efficient solution to the problem.
```

Runtime: undefined
Memory: 19812000
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return [0, None]
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return [left[0] +1, left[1]]
            elif right[0]>left[0]:
                return [right[0]+1, right[1]]
            else:
                return [right[0]+1, root]
        return dfs(root)[1]

