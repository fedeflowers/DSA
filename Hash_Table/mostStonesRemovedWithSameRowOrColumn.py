"""
```markdown
## Explanation of the LeetCode Solution for "Most Stones Removed with Same Row or Column"

### 1. Approach Explanation

The problem requires us to determine the maximum number of stones that can be removed if we can only remove stones from the same row or the same column. The approach taken in this solution involves treating the stones as nodes in a graph, where each stone can connect to others in the same row or column. Therefore, the first step is to group the stones based on their x and y coordinates using two dictionaries.

The `removeStones` function works as follows:

- **Mapping Stones**: We create two dictionaries: `rows` and `cols`. For each stone represented by its coordinates (x, y), we add its index to the corresponding list in `rows` (for the x-coordinate) and `cols` (for the y-coordinate).

- **DFS for Connected Components**: We then use depth-first search (DFS) to explore all stones connected directly or indirectly through other stones in the same row or column. Each time we initiate a DFS from a new stone, it signifies a new connected component of stones.

- **Counting Components**: The number of connected components corresponds to the number of distinct groups of stones that cannot be removed together due to their connections. The maximum stones that can be removed is equal to the total number of stones minus the number of these components.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(N), where N is the number of stones. This is because we traverse through all stones to build the connections and again for each stone during the DFS, ensuring every stone is visited once.

- **Space Complexity**: The space complexity is also O(N) due to the storage required for the `rows` and `cols` dictionaries and the `visited` list. In the worst-case scenario, where all stones are in distinct rows and columns, the space utilized will scale linearly with the number of stones.

### 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Graph Representation**: By representing the stones as nodes connected through shared rows and columns, we can utilize graph traversal techniques which are well-suited to this type of connectivity problem.

- **Direct Component Counting**: The solution effectively counts connected components rather than trying to simulate removal, which can become cumbersome. This provides a more straightforward calculation of removable stones.

- **Single Pass DFS**: By employing a single DFS from each unvisited stone, we ensure each stone is processed only once, making the solution both efficient and scalable.

Overall, this method efficiently determines the maximum number of removable stones while minimizing the complexity of the implementation.
```

Runtime: undefined
Memory: 21388000
"""

class Solution:
    def removeStones(self, stones):
        # Map each x and y coordinate to a list of stone indices
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        visited = [False] * len(stones)
        num_components = 0

        def dfs(stone_idx):
            visited[stone_idx] = True
            x, y = stones[stone_idx]
            
            # Visit all stones in the same row
            for neighbor in rows[x]:
                if not visited[neighbor]:
                    dfs(neighbor)
            
            # Visit all stones in the same column
            for neighbor in cols[y]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(len(stones)):
            if not visited[i]:
                dfs(i)
                num_components += 1

        return len(stones) - num_components
