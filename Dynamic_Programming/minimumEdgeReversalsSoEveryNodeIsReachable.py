"""
### Explanation of the Approach

The provided solution tackles the problem of determining the minimum edge reversals needed so that every node in a directed graph (defined by given edges) is reachable from any other node. 

1. **Graph Representation**: The graph is represented using an adjacency list where each directed edge from `u` to `v` is stored as `(v, 0)` indicating a direct edge, and the reverse edge (to indicate reversal) as `(u, 1)` indicating that this edge needs a reversal.

2. **Initial DFS Traversal**: A Depth-First Search (DFS) is conducted starting from node `0` to count the total number of edge reversals required for node `0` to reach all other nodes. This count is stored in `ans[0]`.

3. **Rerooting DFS**: After calculating the reversals needed for node `0`, a second DFS is performed to re-root the graph from any node that has already been processed. This adjusts the reversal counts for all its neighboring nodes based on whether the edge connecting them is directed in the expected direction or if it would need to be reversed. 

4. **Final Result**: After rerooting, the array `ans` will contain the minimum edge reversals needed for each node in the graph to ensure every other node is reachable.

### Time and Space Complexity Analysis

- **Time Complexity**: The algorithm runs in O(N), where N is the number of nodes in the graph. Each node and edge is visited exactly twice (once during the initial DFS and once during the rerooting DFS), leading to linear traversal complexity.

- **Space Complexity**: The space complexity is also O(N) primarily due to the adjacency list storage for the graph. Additionally, the recursion stack depth for DFS could also take O(N) in the worst case (for balanced trees, for example).

### Why This Approach is Efficient

1. **Linear Traversal**: Both the initial DFS and rerooting DFS traverse each node and edge once, making the algorithm efficient especially for large graphs, as this ensures minimal overhead.

2. **Use of Rerooting**: The rerooting technique allows for recalculating reversals based on changing perspectives (which node is currently viewed as the root). This helps in eliminating the need for redundant traversals of the already calculated nodes, enhancing performance.

3. **Memory Efficiency**: By using an adjacency list instead of matrix representations, space complexity is kept reasonable, especially in sparse graphs.

In conclusion, this solution effectively utilizes graph traversal techniques to compute the required reversals in an optimal manner, making it both time and space efficient for solving the problem at hand.

Runtime: undefined
Memory: 179636000
"""

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0)) # Original edge
            adj[v].append((u, 1)) # Needs reversal

        ans = [0] * n

        # Step 1: DFS from node 0 to find its total reversals
        def dfs_initial(u, p):
            total = 0
            for v, weight in adj[u]:
                if v != p:
                    total += weight + dfs_initial(v, u)
            return total

        ans[0] = dfs_initial(0, -1)

        # Step 2: Re-rooting DFS to find reversals for all other nodes
        def dfs_reroot(u, p):
            for v, weight in adj[u]:
                if v != p:
                    # If weight is 0 (u->v), moving to v adds 1 reversal (v->u)
                    # If weight is 1 (v->u), moving to v removes 1 reversal (v already reaches u)
                    ans[v] = ans[u] + (1 if weight == 0 else -1)
                    dfs_reroot(v, u)

        dfs_reroot(0, -1)
        return ans
