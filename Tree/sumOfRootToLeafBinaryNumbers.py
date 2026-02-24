"""
## Explanation of the LeetCode Solution for "Sum of Root to Leaf Binary Numbers"

### 1. Approach Explanation

The problem requires us to calculate the sum of all the binary numbers represented by root-to-leaf paths in a binary tree. Each node in the binary tree contains a value either 0 or 1. To represent the binary number from the root to any leaf, we concatenate the values of the nodes along the path.

The solution employs a Depth-First Search (DFS) strategy to traverse the binary tree. Here's a breakdown of the key components:

- **DFS Function**: The `dfs` function takes two parameters: the current node (`root`) and the sum accumulated so far (`curr_sum`). If the current node is a leaf (both left and right children are `None`), it computes the binary number represented by the path up to that leaf by shifting the current sum left (`curr_sum << 1`) and adding the value of the current node (`root.val`).

- **Recursion**: If the current node has left or right children, the function recursively calls `dfs` for both sides, updating the `curr_sum` accordingly for both the left and right child nodes.

- **Base Case**: When a leaf node is reached, it returns the computed binary number. The left and right sums from the respective child nodes are accumulated and returned to the previous level.

Finally, the initial call to `dfs` is made with the root node and `0` as the initial sum.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(N), where N is the number of nodes in the binary tree. We visit each node exactly once during the DFS traversal.

- **Space Complexity**: The space complexity is O(H), where H is the height of the tree. This is due to the call stack used by the recursive DFS function. In the worst-case scenario (a skewed tree), H can be equal to N. However, in a balanced binary tree, H would be approximately log(N).

### 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Direct Calculation**: The method calculates the binary value on-the-fly instead of building a separate data structure to store each path's binary number. This reduces space usage.
  
- **Single Pass**: By using DFS, the algorithm processes each node once, making it optimal in terms of time complexity. 

- **Early Return**: It immediately computes the result when it reaches a leaf node, which minimizes unnecessary calculations.

Overall, the DFS implementation provides an optimal and straightforward solution to the problem, efficiently summing up all the root-to-leaf binary numbers in a single traversal of the tree.

Runtime: undefined
Memory: 19760000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr_sum):
            if not root.left and not root.right:
                return (curr_sum << 1) + root.val
            left = 0
            right = 0
            if root.left:
                left += dfs(root.left, (curr_sum << 1) + root.val)
            if root.right:
                right += dfs(root.right, (curr_sum << 1) + root.val)
            return left + right

        return dfs(root, 0)


