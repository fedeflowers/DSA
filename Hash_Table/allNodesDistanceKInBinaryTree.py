"""
## Explanation of the LeetCode Solution for "All Nodes Distance K in Binary Tree"

### 1. Approach

This solution tackles the problem by first converting the binary tree into an undirected graph. This is done using a depth-first search (DFS) to create an adjacency list representation, where each node maps to its neighbors (parent and children). Once the graph is constructed, a DFS is performed starting from the given target node to find and return all nodes that are exactly `k` distance away.

The steps are as follows:
- **Graph Construction**: A helper function `create_graph` builds the graph based on the binary tree structure. It traverses the tree and connects each node to its neighbors (parent and children).
- **Distance Search**: A DFS function `dfs` is then employed to find nodes at exactly `k` distance from the target node. It avoids revisiting nodes by maintaining a set of visited nodes.

### 2. Time and Space Complexity

- **Time Complexity**: 
  - The graph construction takes O(N) time, where N is the number of nodes in the tree because every node and edge is processed once.
  - The DFS traversal to collect nodes at distance `k` also takes O(N) time in the worst case, since all nodes may need to be explored.
  - Therefore, the overall time complexity is O(N).

- **Space Complexity**:
  - The space complexity is primarily due to the storage of the graph, which would also hold up to O(N) entries (for each node and its edges).
  - The recursive call stack in the DFS could go up to O(H) where H is the height of the tree.
  - Thus, the total space complexity is O(N) due to the graph storage, with an additional O(H) for the recursion stack.

### 3. Efficiency of the Approach

This approach is efficient because:
- **Graph Construction**: By transforming the tree into an undirected graph, it allows for easy traversal and neighbor discovery without concern for direction (like the typical parent-child structure of trees).
- **DFS Usage**: The usage of DFS ensures that we can explore each node's neighbors efficiently and reach nodes at distance `k` without redundant checks, thanks to the visited tracking system.
- **Scalability**: The algorithm scales well with the size of the binary tree since both its time and space complexities are linear with respect to the number of nodes.

Overall, the combination of graph construction and efficient traversal enables quick resolution of the target distance queries.

Runtime: undefined
Memory: 17720000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list) # node : [neighbours]
        def create_graph(root: TreeNode, parent: TreeNode) -> dict:
            if not root:
                return
            if root and parent:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)

            create_graph(root.left, root)
            create_graph(root.right, root)

        create_graph(root, None)

        res = []
        visited = set()
        #DFS or BFS
        def dfs(node: int, k:int):
            if node in visited:
                return
            
            visited.add(node)
                
            if k == 0:
                res.append(node)
            for neigh in graph[node]:
                dfs(neigh, k-1)

            

        dfs(target.val, k)
        return res


