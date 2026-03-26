"""
## Explanation of Solution for "Invert Binary Tree"

### 1. Brief Explanation of the Approach
The provided solution uses a recursive depth-first search (DFS) approach to invert a binary tree. The function `invertTree` takes a `TreeNode` object `root`, which represents the root of the binary tree. The process is as follows:

- **Base Case**: If the `root` is `None` (indicating an empty subtree), the function returns `None`.
- **Recursive Inversion**: If the `root` is not `None`, the function recursively calls itself to invert the right subtree first and then the left subtree. The results of these calls are then swapped. 
- **Simultaneous Assignment**: This assignment operation is done simultaneously, ensuring that the original references to left and right children are effectively swapped in the same step.
- Finally, the function returns the `root`, which now represents the inverted binary tree.

Example: For a tree structured like this:
```
    1
   / \
  2   3
```
After calling `invertTree`, it transforms to:
```
    1
   / \
  3   2
```

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. This is because the algorithm needs to visit each node exactly once to perform the inversion.
  
- **Space Complexity**:
  - The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack used during the traversal of the tree. In the case of a balanced tree, h is O(log N), but in the worst case (skewed tree), h could be O(N).
  
### 3. Why This Approach is Efficient
This approach is efficient for several reasons:

- **Simplicity**: The recursive algorithm is straightforward and easy to understand. It leverages the properties of trees and recursion effectively, avoiding unnecessary complexity.
- **DFS**: The depth-first traversal ensures we process each node while making the minimal number of passes (only one pass is needed to invert the tree).
- **In-Place Modification**: Since the inversion is done by swapping the child pointers directly, it doesn't require any additional data structures or storage for another tree, making optimal use of memory.
- **Independence from Tree Structure**: The method works well regardless of the shape of the tree (balanced, skewed, complete, etc.), maintaining a consistent time complexity of O(N).

Overall, this approach efficiently inverts a binary tree while keeping the implementation clean and understandable.

Runtime: undefined
Memory: 19292000
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Simultaneous swap ensures both original references are used
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
