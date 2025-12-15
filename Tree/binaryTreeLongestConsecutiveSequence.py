"""
# Explanation of the Solution for "Binary Tree Longest Consecutive Sequence"

## 1. Brief Explanation of the Approach
The problem "Binary Tree Longest Consecutive Sequence" aims to find the length of the longest consecutive sequence path in a binary tree, where each node's value is exactly 1 more than its parent’s value. The solution uses Depth-First Search (DFS) to traverse the tree.

The approach involves the following steps:
- We define a recursive function `dfs(root, path)` that takes a node (`root`) and the current length of the consecutive path (`path`).
- If the current node is `None`, the function returns the current path length.
- For each child node (left and right), it checks if the child value is equal to the current node value + 1:
  - If true, it calls `dfs` on the child with `path + 1`.
  - If false, it resets the path length to 1 and calls `dfs` on the child.
- Throughout the traversal, we maintain a variable `longest` that holds the maximum path length found.
- Finally, the result is returned after traversing the entire tree.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)  
  The algorithm visits each node exactly once, where N is the number of nodes in the tree. Traversing the tree in a depth-first manner ensures that every node is processed, making the time complexity linear with respect to the number of nodes.

- **Space Complexity**: O(H)  
  The space complexity is determined by the recursion stack used by depth-first search. In the worst case of a skewed tree (essentially a linked list), the maximum depth of the recursion stack is equal to the height of the tree, denoted as H. In a balanced tree, the height would be log(N), hence O(H) is acceptable.

## 3. Why This Approach is Efficient
The DFS approach is efficient for several reasons:
- **Direct Processing**: Each node is processed once, leading to a linear run-time.
- **Path Tracking**: The recursive nature of DFS allows easy tracking of the length of consecutive paths without needing additional data structures, leading to streamlined memory usage.
- **Compact Code**: The logic is straightforward and clearly reflects the constraints of the problem, making it easier to extend or modify if needed.
- **Early Exit**: As soon as a node's children are processed, the function returns, which minimizes unnecessary checks and further enhances performance.

Overall, the solution is concise, easy to understand, and efficiently tackles the problem by directly leveraging the properties of DFS in tree traversal.

Runtime: undefined
Memory: 21244000
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

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        #DFS
        longest = 0
        def dfs(root, path):
            nonlocal longest
            if not root:
                return path

            if root.left:
                if root.left.val == root.val + 1:
                    l = dfs(root.left, path + 1)
                else:
                    l = dfs(root.left, 1)

            if root.right:
                if root.right.val == root.val + 1:
                    r = dfs(root.right, path + 1)
                else:
                    r = dfs(root.right, 1)
                
            # longest = max(r, l)
            longest = max(longest, path)
            return path
        
        dfs(root, 1)
        return longest
