"""
### Explanation of the Approach

The problem "Most Stones Removed with Same Row or Column" involves determining how many stones can be removed from a grid while ensuring that each removal of a stone is connected through either the same row or the same column with other stones. This task can be visualized as a graph where each stone can be considered a node, and edges can exist between stones that share the same row or column.

The solution uses a graph traversal technique (DFS) to find connected components of stones. Here’s a breakdown of the approach:

1. **Adjacency List Creation**: 
   - Two dictionaries, `x_adj` and `y_adj`, are created to store lists of stone indices that share the same x-coordinate (row) and y-coordinate (column), respectively.
   - For each stone (given as coordinates [x, y]), the index of that stone is appended to both `x_adj[x]` and `y_adj[y]`.

2. **Graph Traversal**: 
   - A Depth-First Search (DFS) function is defined to explore the connected stones. 
   - Starting from an unvisited stone, DFS will traverse all stones connected directly or indirectly via rows or columns and mark them as visited.

3. **Counting Components**: 
   - The main loop iterates through each stone. If a stone hasn't been visited, it indicates the start of a new connected component, so the component count is incremented and DFS is invoked.
   
4. **Result Calculation**: 
   - The result is calculated as the total number of stones minus the number of connected components. This result represents the maximum number of stones that can be removed while keeping at least one stone in each component.

### Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - Each stone is processed once in creating the adjacency list, and each stone is again processed during the DFS traversal. Therefore, the total time complexity is proportional to the number of stones (N).

- **Space Complexity**: O(N)
  - The space used for storing the adjacency list (both `x_adj` and `y_adj`) requires space proportional to the number of stones since we are storing the index of each stone. The visited set also stores up to N elements in the worst case.

### Why This Approach is Efficient

This approach is efficient because it effectively reduces the problem to finding connected components in a graph representation of the stones:

1. **Scalability**: The use of adjacency lists allows for efficient connections between stones based on shared rows or columns, making it scalable for a large number of stones.

2. **Optimal Traversal**: DFS efficiently explores all connections along rows and columns, ensuring that all reachable stones are visited without unnecessary re-visits. 

3. **Direct Problem-solving**: The method directly addresses the problem's requirement (maximum removable stones while maintaining connectivity) by abstracting it to a graph theory problem—finding connected components.

Overall, the solution is optimal and leverages graph theory principles to achieve the desired result effectively.

Runtime: undefined
Memory: 22296000
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        #adj list
        x_adj = defaultdict(list)
        y_adj = defaultdict(list)

        for i, (x,y) in enumerate(stones):
            x_adj[x].append(i)
            y_adj[y].append(i)
        
        visited = set()
        #dfs
        def dfs(index):
            visited.add(index)
            x, y = stones[index]
            for i in x_adj[x]:
                if i not in visited:
                    dfs(i)
                    
            for i in y_adj[y]:
                if i not in visited:
                    dfs(i)
     
        components = 0
        for i in range(len(stones)):
            if i not in visited:
                components += 1
                dfs(i)
        
        return len(stones) - components
