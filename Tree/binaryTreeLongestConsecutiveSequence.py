"""
## Explanation of the Approach

The solution to the "Binary Tree Longest Consecutive Sequence" problem uses an iterative breadth-first search (BFS) approach to traverse the binary tree and find the longest consecutive sequence of values. 

1. **Initialization**: We start by initializing a variable `longest` to keep track of the longest consecutive sequence found so far. If the root is `None`, the function immediately returns `0`.

2. **Queue Setup**: A queue (using `Deque` from `collections`) is initialized to facilitate the BFS. Each entry in the queue consists of a tuple containing a tree node and the current length of the consecutive sequence leading up to that node.

3. **BFS Traversal**:
   - While the queue is not empty, we dequeue the front element, which gives us the current node and its corresponding path length.
   - We update the `longest` variable with the maximum value between the current `longest` and the `path` length.
   - For each child node, we check if it is a consecutive child (i.e., `child.val` equals `parent.val + 1`):
     - If it is, we increment the path length and enqueue the child node with the new path length.
     - If not, we reset the path length to `1` (indicating a new potential sequence).
  
4. **Result**: After finishing the traversal, the `longest` variable is returned, which represents the length of the longest consecutive sequence found in the tree.

## Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once throughout the BFS traversal.
  
- **Space Complexity**: O(W), where W is the maximum width of the binary tree. In the worst case, this could be approximately O(N) if the tree is completely unbalanced (like a linked list). In a balanced scenario, this would tend to be closer to O(log N).

## Why This Approach Is Efficient

- The BFS approach ensures that all nodes are processed in a systematic manner while checking for consecutive sequences.
- By maintaining the current path length as we traverse, the algorithm efficiently tracks the length of sequences without the need for extra space for parent-child relationships.
- This method avoids the overhead of recursion and stack memory usage, making it suitable for large trees where recursion depth could be a concern. The use of a queue allows for managing nodes in a first-in-first-out manner, ensuring all levels of the tree are processed thoroughly before moving on.

Runtime: undefined
Memory: 20540000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 0
        if not root:
            return longest

        q = Deque([(root, 1)])
        while q:
            root, path = q.popleft()
            longest = max(longest, path)
            if root.left:
                if root.left.val == root.val + 1:
                    q.append([root.left, path + 1])
                else:
                    q.append([root.left, 1])
            if root.right:
                if root.right.val == root.val + 1:
                    q.append([root.right, path + 1])
                else:
                    q.append([root.right, 1])
                
        return longest
