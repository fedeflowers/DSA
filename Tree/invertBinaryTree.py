"""
# LeetCode Solution Explanation for "Invert Binary Tree"

## 1. Brief Explanation of the Approach
The solution to the "Invert Binary Tree" problem involves a recursive approach to invert the binary tree. The key idea is to swap the left and right children of each node in the tree. 

- The function `invertTree` takes in a node (`root`) of a binary tree.
- If the current node is `None`, it returns `None`, which serves as the base case for the recursion.
- For non-null nodes, it swaps the left and right children of the current node.
- After swapping, it recursively calls the `invertTree` function on the left and right children to ensure all levels of the tree are inverted.
- Finally, it returns the root of the inverted tree.

## 2. Time and Space Complexity Analysis
- **Time Complexity:** O(N)
  - Here, N is the number of nodes in the binary tree. The algorithm visits each node exactly once to perform the swapping operation and the recursive calls. Hence, the overall time complexity is linear with respect to the number of nodes.

- **Space Complexity:** O(H)
  - H is the height of the binary tree. The maximum space used on the call stack due to recursion is proportional to the height of the tree. In the worst case (unbalanced tree), this could be O(N), but for a balanced tree, the height will be O(log N).

## 3. Why This Approach is Efficient
This approach is efficient because:

- **Simplicity:** The solution is straightforward, easily understandable, and clean due to its recursive nature.
- **Optimal Node Visit:** Each node is handled exactly once, ensuring that the algorithm runs in linear time, making it efficient for any size binary tree.
- **In-Place Modification:** The inversion is done in place, meaning we utilize the existing nodes and do not require additional data structures to store nodes, leading to optimal space usage for tree inversion.

Overall, this approach is efficient and elegant while effectively solving the problem of inverting a binary tree.

Runtime: undefined
Memory: 19228000
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
