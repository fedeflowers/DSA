"""
## Explanation of the Approach

The problem "All Nodes Distance K in Binary Tree" requires us to find all nodes that are exactly K distance away from a given target node in a binary tree. The solution follows these steps:

1. **Graph Construction**: The binary tree is first transformed into an undirected graph representation. This is done using Depth-First Search (DFS) to establish connections between each node and its neighboring nodes (its parent and children).

2. **Traversal**: Once the graph is built, a Breadth-First Search (BFS) is used to traverse the graph starting from the `target` node. It explores all neighbors at the current distance before moving on to nodes at the next distance level.

3. **Collect Results**: During the BFS, once the distance from the target node reaches `k`, the current node is added to the result list.

The primary data structures used are a graph represented as an adjacency list and a queue for BFS traversal.

## Time and Space Complexity Analysis

### Time Complexity
- **Graph Construction**: This process visits each node in the tree once, so it runs in \(O(N)\), where \(N\) is the number of nodes in the binary tree.
- **BFS Traversal**: Similarly, the BFS visits each node and edge once as well, leading to another \(O(N)\) complexity.
  
Overall, the time complexity is:
\[ O(N) + O(N) = O(N) \]

### Space Complexity
- **Graph Storage**: The space used to store the graph as an adjacency list requires \(O(N)\).
- **Visited Set**: The visited set could contain up to \(N\) nodes in the worst case.
- **Queue**: The queue used for BFS can also store up to \(N\) elements, although in practice it will usually contain far fewer.

Thus, the overall space complexity is:
\[ O(N) + O(N) + O(N) = O(N) \]

## Why This Approach is Efficient
This approach is efficient for several reasons:

1. **Conversion to Graph**: The transformation of the binary tree into a graph allows for straightforward traversal that can capture connections in both directions (parent to child and child to parent), making it easy to navigate whenever needed.

2. **BFS for Layered Traversal**: Using BFS ensures that all nodes at the same distance level from the target are processed before moving deeper, effectively managing the K distance requirement with minimal overhead.

3. **Single Pass for Each Step**: Both the graph construction and BFS traversal are performed in linear time with respect to the number of nodes, making the entire algorithm efficient and suitable for large trees.

This combination of a well-structured graph and an efficient traversal method allows the solution to handle various sizes of binary trees comfortably, maintaining performance.

Runtime: undefined
Memory: 17668000
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
        
        # visited = set()    
        # res = []   
        # DFS
        # def dfs(node, distance):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     if distance == k:
        #         res.append(node)
        #     for child in graph[node]:
        #         dfs(child, distance+1)

        # dfs(target.val, 0)
        # return res

        #BFS
        visited = set([target.val])    
        res = []  
        q = Deque([(target.val,0)])
        while q:
            node, d = q.popleft()
            if d == k:
                res.append(node)
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.append((child, d+1))
        return res





            
            
