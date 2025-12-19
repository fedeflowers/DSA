"""
# Explanation of LeetCode Solution for "All Nodes Distance K in Binary Tree"

## 1. Brief Explanation of the Approach

The solution to the problem of finding all nodes that are a distance `K` from a target node in a binary tree can be accomplished through a depth-first search (DFS) approach. The strategy is divided into two main parts:

- **Traversal and Depth Calculation**: The solution uses a recursive function `dfs` to traverse the binary tree. The goal is to find the target node and calculate the distance from it to its parent nodes, while also processing the left and right children during the backtracking phase. 

- **Collecting Nodes at Distance K**: Once the target node is found, the function `collect` is called to collect all nodes from the target downward that are `K` levels deep. Additionally, while backtracking up the tree, if the distance to the parent node equals `K`, that node is also added to the result. If not, the algorithm calls `collect` on the sibling branch to check for nodes that may be at distance `K`.

Overall, this solution efficiently combines DFS traversal with a strategy to backtrack and explore both subtrees.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is `O(N)`, where `N` is the number of nodes in the binary tree. This is because every node is visited once during the DFS traversal.

- **Space Complexity**: The space complexity is `O(H)`, where `H` is the height of the binary tree. This includes the space for the recursion stack during the DFS. The output list for the result also contributes to the space used, but in the worst case (if all nodes are at distance `K`), the output space is `O(N)`. However, since the recursion stack is the limiting factor, we generally consider the space complexity as `O(H)`.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

1. **No Additional Data Structures Required**: Unlike alternative methods (e.g., constructing a full adjacency list for graph representation), this solution navigates the tree using its inherent structure, eliminating the need for extra space besides the necessary recursion stack and output list.

2. **Single Pass for Target Location and Distance Calculation**: The method finds the target node and processes necessary nodes in a single traversal (DFS). This reduces overhead compared to separate searches.

3. **Effective Backtracking**: By handling both downward (collecting nodes `K` levels down from the target) and upward (checking for parent nodes at a specific distance), the approach fully exploits the binary tree's structure and minimizes repeated work.

4. **Handles Edge Cases**: The solution accounts for all necessary distances, including nodes not directly connected to the target node but are reachable at distance `K`, making it robust for varying inputs.

Overall, this method efficiently provides the answer without excessive operations or memory usage, making it suitable for large binary trees while ensuring clarity and correctness in the traversal logic.

Runtime: undefined
Memory: 17672000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
#         graph = defaultdict(list) # node : [neighbours]
#         def create_graph(root: TreeNode, parent: TreeNode) -> dict:
#             if not root:
#                 return
#             if root and parent:
#                 graph[root.val].append(parent.val)
#                 graph[parent.val].append(root.val)

#             create_graph(root.left, root)
#             create_graph(root.right, root)

#         create_graph(root, None)

#         res = []
#         visited = set()
#         #DFS or BFS
#         def dfs(node: int, k:int):
#             if node in visited:
#                 return
            
#             visited.add(node)
                
#             if k == 0:
#                 res.append(node)
#             for neigh in graph[node]:
#                 dfs(neigh, k-1)

            

#         dfs(target.val, k)
#         return res

# NO GRAPH T: O(N), M: O(H)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def collect(root, distance):
            if not root:
                return
            if distance == 0:
                res.append(root.val)
                return

            collect(root.left, distance-1)
            collect(root.right, distance-1)

        def dfs(root):
            if not root:
                return -1 #not found

            if root == target:
                collect(root, k) #si cerca quelli sotto 
                return 0

            L = dfs(root.left)
            #in backtracking cerco gli altri nodi
            if L != -1: # != se è 0 quindi ho trovato o la distance
                dist = L + 1 #+1 perchè sono in backtracking quindi sono già tornato al nodo parent
                if dist == k: res.append(root.val)
                #-dist perchè è da dove chiamo la collect, -1 perchè sto chiamando il nodo dell'altro branch
                else: collect(root.right, k - dist - 1) #chiamo collect su altro branch, perchè lì non ho ancora visitato e potrei trovare nodi a distanza k, (il target l'ho già trovato)
                return dist

            R = dfs(root.right)
            if R != -1:
                dist = R + 1
                if dist == k: res.append(root.val)
                else: collect(root.left, k - dist -1)
                return dist

            return -1 #not found

        dfs(root)
        return res


