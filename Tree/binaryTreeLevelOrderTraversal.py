"""
## Explanation of the Solution for "Binary Tree Level Order Traversal"

### 1. Approach Explanation
The given solution utilizes a breadth-first search (BFS) approach to perform a level order traversal of a binary tree. The main idea is to explore each level of the tree before moving on to the next level. This is effectively done using a queue data structure which facilitates FIFO (First In First Out) processing. 

Here's a breakdown of the steps involved in the solution:

- **Initialization**: We start by checking if the `root` is `None`. If it is, we return an empty list because there are no nodes to traverse.
- **Queue Setup**: A queue (using `deque` for efficiency) is initialized with the `root` node. An empty list called `order` is prepared to store the final result of the level order traversal.
- **Processing Each Level**: We enter a loop that continues until the queue is empty:
  - We determine the number of nodes at the current level by checking the length of the queue (`level_len`).
  - An empty list called `level` is created to capture the values of the nodes at this level.
  - We perform another loop that runs `level_len` times to process each node in the current level:
    - We dequeue a node from the front of the queue.
    - We append its value to the current `level` list.
    - If it has a left child, we enqueue that child.
    - If it has a right child, we enqueue that child.
  - After processing all nodes at the current level, we append the `level` list to the `order` list.
- **Final Output**: Once all levels have been processed, we return the `order` list, which now contains the values grouped by their respective levels in the tree.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - Here, `N` is the number of nodes in the binary tree. Each node is visited exactly once, and thus the time taken is linear with respect to the number of nodes.
  
- **Space Complexity**: O(N)
  - In the worst case (a completely unbalanced tree, such as a degenerate tree), the queue can store up to `N` nodes in the last level. Therefore, the space complexity is also linear with respect to the number of nodes in the tree.

### 3. Efficiency of the Approach
This BFS-based approach is efficient for level order traversal because:
- It guarantees that nodes are processed level by level, which is the primary requirement of the problem.
- The use of the queue ensures that we efficiently manage the nodes as they are added and removed, mimicking the natural breadth-first traversal of the tree.
- The overall linear time complexity makes this solution scalable to large binary trees, as it only requires a single traversal of the tree to complete the task.
- The memory footprint, while also O(N), is necessary for the structure of binary trees when fully populated, making this trade-off acceptable. 

In summary, the approach effectively combines clarity and performance for the problem at hand, making it a standard solution for level order traversal tasks.

Runtime: undefined
Memory: 19860000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        order = []
        queue = deque([root])
        while queue:
            level_len = len(queue)
            level = []
            for _ in range(level_len):
                el = queue.popleft()
                level.append(el.val)
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            order.append(level)


        return order
