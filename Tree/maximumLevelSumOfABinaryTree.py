"""
## Explanation of the Approach

The provided solution uses a depth-first search (DFS) traversal to calculate the sum of each level in a binary tree and subsequently determines which level has the maximum sum. Here’s a step-by-step breakdown of the logic:

1. **Level Tracking**: A list called `level_sums` is used to store the cumulative sums of the nodes at each level of the binary tree. The index of the list corresponds to the tree level, starting from level 0 (the root level).

2. **Recursive Function**: A helper function `dfs(node, level)` is defined:
   - It accepts the current `node` and its `level`.
   - If the current `node` is None (base case), the function returns.
   - If it’s the first time reaching this `level`, it initializes the sum for this level with the node’s value. Otherwise, it adds the current node's value to the existing sum at that level.
   - The function recursively calls itself for the left and right children of the current node, incrementing the level by 1.

3. **Finding Maximum Level Sum**: After populating the `level_sums` list, the algorithm identifies the maximum sum among the levels. It then iterates through the `level_sums` to find the index (level) with this maximum sum. In case of ties (equal sums), it returns the lowest level (smallest index), ensuring the correct level is returned as per the problem's requirements.

---

## Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - The function visits each node exactly once, where N is the number of nodes in the binary tree. Thus, the time complexity is linear with respect to the number of nodes.

- **Space Complexity**: O(H)
  - The space complexity is influenced mainly by the call stack during the depth-first traversal, which can go as deep as the height H of the tree. In addition, if the tree is well-balanced, the height H would be O(log N), but in the worst case (a degenerate tree resembling a linked list), the height would be O(N). There is also O(L) space for storing the level sums, where L is the maximum number of levels (which would be O(N) in the worst case), but this is generally dominated by the height-related recursion space.

---

## Why This Approach is Efficient

- **Logical Depth-First Traversal**: The use of DFS allows traversing the tree in a straightforward manner while simultaneously calculating the required sums. This avoids the need for more complex data structures for level tracking and prevents unnecessary additional space usage for intermediate storage.

- **Single Pass Calculation**: By combining the traversal and summation processes, the algorithm is efficient and minimizes redundant calculations. Each node's value is added at the moment it is visited.

- **Clear Handling of Ties**: The approach efficiently handles the requirement to return the smallest level in case of maximum sum ties, ensuring that the solution adheres to the problem constraints without additional checks or complications.

Overall, this solution remains optimal for binary tree level sum calculation due to its simplicity, efficiency, and clarity in handling different aspects of the problem.

Runtime: undefined
Memory: 22892000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         q = Deque([root])
#         max_sum = -float("inf")
#         final_level = 1
#         curr_level = 1
#         while q:
#             level_size = len(q)
#             level_sum = 0
#             for _ in range(level_size):
#                 curr_node = q.popleft()
#                 level_sum += curr_node.val
#                 if curr_node.left != None:
#                     q.append(curr_node.left)
#                 if curr_node.right != None:
#                     q.append(curr_node.right)
#             if level_sum > max_sum:
#                 max_sum = level_sum
#                 final_level = curr_level
#             curr_level += 1
            

#         return final_level

class Solution:
    def maxLevelSum(self, root):
        level_sums = []

        def dfs(node, level):
            if not node:
                return
            # If this is the first time reaching this level, initialize it
            if len(level_sums) == level:
                level_sums.append(node.val)
            else:
                level_sums[level] += node.val
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        
        # Return level index + 1 of the maximum sum
        # Use -max() to ensure we pick the smallest level in case of ties
        max_sum = max(level_sums)
        for i, s in enumerate(level_sums):
            if s == max_sum:
                return i + 1

        
        
