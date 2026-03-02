"""
```markdown
# Explanation of LeetCode Solution for "Diameter of Binary Tree"

## 1. Approach Explanation
The solution uses a Depth-First Search (DFS) strategy to calculate the diameter of a binary tree. The diameter is defined as the length of the longest path between any two nodes in the tree. This path may or may not pass through the root. 

### Key Steps:
- The function `diameterOfBinaryTree` initializes a variable `max_diameter` to negative infinity, which will be updated during DFS traversal to track the maximum diameter found.
- A helper function `dfs` is defined to perform the DFS traversal. It takes a node as an argument and returns the height of the subtree rooted at that node.
- In each recursive call of `dfs`:
  - If the current node is `None`, it returns 0 (base case).
  - It recursively calls itself to find the heights of the left and right subtrees.
  - The diameter at the current node is calculated as the sum of the heights of the left and right subtrees (`left + right`).
  - `max_diameter` is updated to be the maximum of its current value and the newly calculated diameter.
  - Finally, the function returns the height of the subtree rooted at the current node, which is `max(left, right) + 1`.
- After the DFS traversal, `max_diameter` is returned as the output representing the diameter of the binary tree.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - In the worst case, we visit every node in the binary tree once, where N is the number of nodes.
  
- **Space Complexity**: O(H)
  - The space complexity is determined by the recursion stack, which in the worst case can go as deep as the height of the tree. H is the height of the binary tree, which could be N in the case of a skewed tree.

## 3. Efficiency of the Approach
This approach is efficient due to:
- **Single Pass DFS**: It computes the diameter while also calculating subtree heights in a single traversal, minimizing redundant calculations.
- **Space Optimization**: It uses the recursion stack efficiently, avoiding the need for additional data structures or lists to store intermediate results, which would increase memory usage.
- **Constant Updates**: The use of `nonlocal` for `max_diameter` allows us to keep track of the maximum diameter encountered during recursion without needing to return multiple values or utilize global variables.

Overall, this solution is an optimal way to find the diameter of a binary tree using depth-first traversal and achieves the desired result in linear time with manageable space usage.
```

Runtime: undefined
Memory: 22236000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = -float("inf")
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            curr_diameter = left + right 
            max_diameter = max(max_diameter, curr_diameter)
            
            return max(left, right) + 1
        
        dfs(root)
        return max_diameter
            
