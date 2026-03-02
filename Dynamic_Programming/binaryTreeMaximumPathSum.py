"""
## Explanation of the LeetCode Solution

### 1. Brief Explanation of the Approach

The solution uses a recursive depth-first search (DFS) strategy to traverse the binary tree and calculate the maximum path sum. The path can originate from any node and can span any direction, including using both left and right children. Here’s how it works:

- A helper function `get_gain(node)` is defined to compute the maximum gain obtainable from each node. It returns the highest gain from the path that can be made using either the left or right child of the node while adding the current node's value.
- At each node:
  - The maximum gains from the left and right subtrees are computed.
  - The current path sum is calculated by adding the node's value to the left and right gains.
  - This path sum is compared with the previously stored maximum (`self.max_val`), and the maximum is updated if the current path sum is greater.
  - Finally, the method returns the maximum gain from the node to its parent.
  
This approach ensures that all potential paths are evaluated while maintaining the highest path sum found.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this algorithm is \(O(N)\), where \(N\) is the number of nodes in the binary tree. This is because each node is visited exactly once during the DFS traversal.
  
- **Space Complexity**: The space complexity is \(O(H)\), where \(H\) is the height of the tree. This is due to the recursive call stack. In the worst case (a skewed tree), the height \(H\) can be \(N\), leading to \(O(N)\) space, but in the average case for a balanced tree, it would be \(O(\log N)\).

### 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Single Pass Calculation**: It calculates the maximum path sum in a single traversal (post-order traversal) of the tree, which optimizes performance by preventing multiple scans of the same nodes.
  
- **Local and Global Computation**: By comparing local path sums and updating a global maximum, it efficiently tracks the best path found. This eliminates the need to store paths and perform additional calculations upon completion of the main traversal.
  
- **Handling Negative Values**: The logic of only considering positive gains from left and right paths ensures that paths yielding negative contributions do not affect the sum, which is crucial for finding the maximum path sum especially when dealing with negative values.

In conclusion, the combination of recursive DFS, single pass evaluation, and smart handling of contributions results in an efficient solution for the given problem.

Runtime: undefined
Memory: 23748000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')

        def get_gain(node):
            if not node:
                return 0

            # Only add gain if it is positive
            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)

            # Update global maximum with path through current node
            current_path_sum = node.val + left_gain + right_gain
            self.max_val = max(self.max_val, current_path_sum)

            # Return the max single-branch gain to the parent
            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return self.max_val
