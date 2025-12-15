"""
```markdown
## Explanation of the LeetCode Solution for "Binary Tree Longest Consecutive Sequence"

### 1. Approach
The solution uses a Depth-First Search (DFS) approach to traverse the binary tree while keeping track of the length of the current consecutive sequence. The function `longestConsecutive` initializes the DFS by checking if the root is not null, and if it is valid, it calls the `dfs` helper function with the `root` node and an initial length of `1`.

In the `dfs` function:
- It first checks if the current node (`node`) is `None`. If so, it returns `0` (base case).
- It calculates the length for the left child node:
  - If the left child exists and its value equals the current node's value plus one, it extends the current length by one; otherwise, it resets the length to `1`.
- Similarly, it calculates the length for the right child node with the same logic.
- Finally, it returns the maximum of the current length, the result from the left subtree, and the result from the right subtree.

The DFS runs until all nodes have been visited, allowing the function to find the longest consecutive sequence along any path from the root to a leaf.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - Each node in the binary tree is visited exactly once. Thus, the time complexity is linear in relation to the number of nodes, N.
  
- **Space Complexity**: O(H)
  - The maximum space in the function call stack during the DFS could go up to the height of the tree (H). So in the case of a balanced tree, this is O(log N), but in the worst case (skewed tree), it can be O(N).

### 3. Efficiency of the Approach
This approach is efficient for several reasons:
- **Single Pass Traversal**: The algorithm only traverses the binary tree once, ensuring that it finds the solution in linear time.
- **Minimal Extra Space Usage**: It does not use any additional data structures that grow with the input size, which keeps the memory footprint low besides the call stack.
- **Immediate Comparison**: The consecutive sequence is checked and updated at every node, allowing it to quickly determine the maximum length without redundant checks.

Overall, the DFS method is optimal for this problem as it accurately captures the essence of traversing through the tree while comprehensively updating the longest consecutive sequence length.
```

Runtime: undefined
Memory: 21352000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        #BFS
        # longest = 0
        # if not root:
        #     return longest

        # q = Deque([(root, 1)])
        # while q:
        #     root, path = q.popleft()
        #     longest = max(longest, path)
        #     if root.left:
        #         if root.left.val == root.val + 1:
        #             q.append([root.left, path + 1])
        #         else:
        #             q.append([root.left, 1])
        #     if root.right:
        #         if root.right.val == root.val + 1:
        #             q.append([root.right, path + 1])
        #         else:
        #             q.append([root.right, 1])
                
        # return longest

# class Solution:
#     def longestConsecutive(self, root: Optional[TreeNode]) -> int:
#         #DFS
#         longest = 0
#         def dfs(root, path):
#             nonlocal longest
#             if not root:
#                 return path

#             if root.left:
#                 if root.left.val == root.val + 1:
#                     l = dfs(root.left, path + 1)
#                 else:
#                     l = dfs(root.left, 1)

#             if root.right:
#                 if root.right.val == root.val + 1:
#                     r = dfs(root.right, path + 1)
#                 else:
#                     r = dfs(root.right, 1)
                
#             # longest = max(r, l)
#             longest = max(longest, path)
#             return path
        
#         dfs(root, 1)
#         return longest


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, length):
            if not node:
                return 0
            
            # Calculate length for left and right children
            left_len = length + 1 if node.left and node.left.val == node.val + 1 else 1
            right_len = length + 1 if node.right and node.right.val == node.val + 1 else 1
            
            # Return the max of current path vs. whatever is found in subtrees
            return max(length, dfs(node.left, left_len), dfs(node.right, right_len))

        return dfs(root, 1) if root else 0
