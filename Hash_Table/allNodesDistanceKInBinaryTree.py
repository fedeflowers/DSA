"""
```markdown
# Explanation of the LeetCode Solution for "All Nodes Distance K in Binary Tree"

## 1. Approach

The solution utilizes a two-step process to find all nodes that are exactly `k` distance away from a given target node in a binary tree. Here’s a step-by-step breakdown of the approach:

- **Creating a Graph Representation**: 
  A graph is constructed using an adjacency list representation where each node (value) maintains a list of its connected nodes (neighbors). This is achieved through a Depth-First Search (DFS) that traverses the binary tree and connects each node to its parent and children. 

- **Finding Nodes at Distance K**: 
  Once the graph is built, another DFS is initiated from the target node. During this traversal, each node is visited, and the distance from the target node is incremented. If the distance reaches `k`, the node is added to the result list. A visited set is used to prevent cycles and re-visiting nodes.

This approach effectively combines the properties of trees and graph traversal to solve the problem efficiently.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  The time complexity is O(N) where N is the number of nodes in the binary tree. This accounts for:
  - Building the graph, which visits each node once.
  - Performing a DFS to find nodes at distance `k`, which also visits nodes linearly.

- **Space Complexity**: 
  The space complexity is O(N) as well. The reasons include:
  - The graph representation consumes O(N) space to store edges (connections).
  - The visited set also uses O(N) space in the worst-case scenario (when all nodes need to be stored).
  - The recursion stack could also occupy space proportional to the height of the tree, which in the worst case (unbalanced tree) can be O(N), but will average to O(log N) for balanced trees.

## 3. Why this Approach is Efficient

This approach is efficient due to its linear time complexity relative to the input size. By transforming the binary tree into a graph, we eliminate the constraints imposed by the tree structure on traversal methods. This allows us to easily access "parent" nodes, which is not directly possible in typical tree traversal techniques. The use of DFS ensures that we explore all potential paths from the target up to the specified distance `k`, making the solution not only efficient but also straightforward and easy to implement.

The combination of building the graph in a single traversal and then performing a controlled exploration ensures that the solution remains optimal for the problem at hand.
```

Runtime: undefined
Memory: 17864000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #create grap and then find distance
        graph = defaultdict(list)
        def create_graph(root, parent):
            if not root:
                return
            if parent and root:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)

            create_graph(root.left, root)
            create_graph(root.right, root)

        create_graph(root, None)
        
        visited = set()    
        res = []   
        # dfs or bfs
        def dfs(node, distance):
            if node in visited:
                return
            visited.add(node)
            if distance == k:
                res.append(node)
            for child in graph[node]:
                dfs(child, distance+1)

        dfs(target.val, 0)
        return res


            
            
