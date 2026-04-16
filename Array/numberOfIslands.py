"""
```markdown
## Explanation of the "Number of Islands" Solution

### 1. Approach
The provided solution employs a Depth-First Search (DFS) strategy to explore the grid of land and water represented as a 2D array of strings. Each '1' in the grid represents land, while '0' represents water. The goal is to count the number of distinct islands, where an island is defined as a group of connected '1's (land) that are connected either horizontally or vertically.

Here's a breakdown of the approach:
- The `numIslands` function iterates over each cell in the grid. Whenever it encounters a '1' that has not been visited yet, it triggers a DFS to explore the entire island.
- The `explore_island` function recursively marks all parts of the island as visited, ensuring not to double count parts of the same island.
- The exploration uses a set named `visited` to track which cells have been processed to prevent re-visiting them.
- After fully exploring one island, it returns 1 to indicate that one complete island has been counted, and this is accumulated in the `res` variable.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: \(O(M \times N)\), where \(M\) is the number of rows and \(N\) is the number of columns in the grid. In the worst-case scenario, we may have to visit every cell in the grid to find all islands.
  
- **Space Complexity**: \(O(M \times N)\) in the worst case for the recursive stack, particularly in cases where all cells are land and form a single connected island. The `visited` set also consumes \(O(M \times N)\) space in the worst case, as it could potentially store information about every cell.

### 3. Efficiency of the Approach
This method is efficient because:
- It systematically explores each unvisited cell only once, ensuring that the counting of islands is done in a single pass through the grid.
- The DFS guarantees thorough exploration of each island without unnecessary re-visitation of cells, thus optimizing the performance.
- By using a set to track visited cells, it can quickly check if a cell has already been processed, ensuring rapid lookups and updates.
  
These factors contribute to the overall efficiency, making the approach both time-effective and space-efficient given the constraints of the problem.
```

Runtime: undefined
Memory: 26968000
"""

class Solution:
    def __init__(self):
        self.num_islands = 0
        self.visited = set()
        
    def explore_island(self, x: int, y: int, grid):
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        if grid[x][y] == '0' or (x, y) in self.visited:
            return 0
        
        self.visited.add((x,y))
        for i, k in dirs:
            new_x, new_y = x + i, y + k
            if 0 <= new_y < len(grid[0]) and 0 <= new_x < len(grid) and grid[new_x][new_y] == '1':  
                self.explore_island(new_x, new_y, grid)

        return 1
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += self.explore_island(i, j, grid)
        return res
