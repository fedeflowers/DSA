"""
## Explanation of the LeetCode Solution for "All Nodes Distance K in Binary Tree"

### 1. Approach Explanation

The solution employs a depth-first search (DFS) strategy to find all nodes that are exactly K distance away from a specified target node in a binary tree. Here's a step-by-step breakdown of the approach:

- **Target Value Identification**: 
  - The solution first checks if the `target` parameter is a `TreeNode` object or an integer; if it's a `TreeNode`, it assigns the value of the target node to `target_val`. 

- **DFS Traversal**: 
  - The `dfs` function traverses the binary tree recursively. It returns the distance from the current node to the target node if found, or -1 if not found.

  - **Base Cases**:
    - If the current node is `None`, it returns -1.
    - If the current node matches the target node, it uses the `collect` function to gather all nodes that are K distance away from this node.

  - **Traversing Left and Right Subtrees**:
    - If the target node is found in the left subtree (indicated by a returned distance L ≠ -1), it calculates the distance to the current node. 
      - If the distance matches K, it adds the current node’s value to the result.
      - If not, it calls `collect` on the right subtree to find nodes K distance away from the current node.
      
    - This process is symmetrical for nodes found in the right subtree.

- **Collect Function**: 
  - The `collect` function is responsible for gathering values of all nodes that are exactly K distance away from a given node. It continues the search until it either hits a distance of K (it adds the node's value to the result) or runs out of nodes.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The worst-case time complexity is \(O(N)\), where \(N\) is the number of nodes in the tree. Each node is visited once during the DFS traversal to either collect the nodes at distance K or to traverse down into the subtrees.

- **Space Complexity**: 
  - The space complexity is \(O(H)\), where \(H\) is the height of the tree. This accounts for the recursion stack used in the DFS, which can go as deep as the height of the tree. In a balanced tree, \(H = O(\log N)\), but in a skewed tree, \(H = O(N)\).

### 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Direct Search**: 
  - It focuses on searching for the target node first and calculating distances to nodes directly from it, rather than constructing additional data structures (like a graph) which would increase overhead.

- **Single Pass**: 
  - By using a single DFS traversal, each node is visited only once, yielding an optimal time complexity of \(O(N)\) in relation to tree size.

- **Dynamic Distance Calculation**: 
  - The method of calculating distances while recursively traversing the tree means that it can effectively gather only the necessary nodes at distance K from the target, avoiding unnecessary checks or computations.

This method achieves the desired results efficiently while maintaining clarity and simplicity in its implementation.

Runtime: undefined
Memory: 17588000
"""

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
#         #create grap and then find distance
#         graph = defaultdict(list)
#         def create_graph(root, parent):
#             if not root:
#                 return
#             if parent and root:
#                 graph[root.val].append(parent.val)
#                 graph[parent.val].append(root.val)

#             create_graph(root.left, root)
#             create_graph(root.right, root)

#         create_graph(root, None)
        
#         # visited = set()    
#         # res = []   
#         # DFS
#         # def dfs(node, distance):
#         #     if node in visited:
#         #         return
#         #     visited.add(node)
#         #     if distance == k:
#         #         res.append(node)
#         #     for child in graph[node]:
#         #         dfs(child, distance+1)

#         # dfs(target.val, 0)
#         # return res

#         #BFS
#         visited = set([target.val])    
#         res = []  
#         q = Deque([(target.val,0)])
#         while q:
#             node, d = q.popleft()
#             if d == k:
#                 res.append(node)
#             for child in graph[node]:
#                 if child not in visited:
#                     visited.add(child)
#                     q.append((child, d+1))
#         return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# NO NEED for GRAPH
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        res = []
        # Support both node object or integer as target
        target_val = target.val if isinstance(target, TreeNode) else target

        def collect(node, d):
            if not node or d < 0: return
            if d == 0:
                res.append(node.val)
                return
            collect(node.left, d - 1)
            collect(node.right, d - 1)

        def dfs(node):
            if not node: return -1
            
            # Case 1: Node is the target
            if node.val == target_val:
                collect(node, k)
                return 0
            
            # Case 2: Target is in left subtree
            L = dfs(node.left)
            if L != -1:
                dist = L + 1
                if dist == k: res.append(node.val)
                else: collect(node.right, k - dist - 1)
                return dist
            
            # Case 3: Target is in right subtree
            R = dfs(node.right)
            if R != -1:
                dist = R + 1
                if dist == k: res.append(node.val)
                else: collect(node.left, k - dist - 1)
                return dist
            
            return -1

        dfs(root)
        return res
