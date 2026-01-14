"""
## Explanation of the LeetCode Solution for "Number of Islands"

### 1. Brief Explanation of the Approach
The solution provided implements a Depth-First Search (DFS) approach to count the number of islands in a grid. Each island is represented by '1's (land) in the grid, and '0's (water) represent the absence of land. The algorithm does the following:

- It initializes a set `self.visited` to keep track of the coordinates of the cells that have already been visited to prevent reprocessing.
- The `explore_island` function is a recursive helper function that explores all the cells connected to the current cell (island) and marks them as visited.
- For each cell in the grid, if it is '1' and not previously visited, it calls `explore_island`, which then marks all adjacent connected '1's as visited (exploring in four directions: right, down, left, and up).
- For each call to `explore_island` that starts on an unvisited '1', it will contribute to the count of islands.

The main function, `numIslands`, iterates through the entire grid and increments a result counter for each unvisitedland cell (island) found, effectively counting the number of islands present.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the number of cells in the grid (if the grid is m x n, then N = m * n). Each cell is visited at most once during the DFS exploration.
  
- **Space Complexity**: O(N) in the worst case if all cells are land ('1'). This is due to the recursion stack and the `visited` set that could potentially store every cell if the entire grid is filled with land.

### 3. Why This Approach is Efficient
The DFS approach is efficient for several reasons:

1. **Direct Exploration**: It directly explores all connected components (island parts) from a single starting point in an efficient manner without the need for additional data structures like a queue (which is often used in BFS).

2. **Avoidance of Redundant Computation**: By marking visited cells, we ensure that no cell is processed more than once, which significantly reduces the number of operations compared to naive approaches that check each cell independently.

3. **Simplicity**: The recursive nature of the DFS algorithm simplifies the logic of traversing connected components, making the code relatively straightforward and easier to understand.

Overall, this method effectively and efficiently counts the number of islands in the given grid by leveraging DFS to explore adjacent land cells, ensuring all parts of each island are accounted for while avoiding unnecessary recomputation.

Runtime: undefined
Memory: 26384000
"""

class Solution:
    def __init__(self):
        self.visited = set()

    def explore_island(self, start, grid):
        x,y = start
        if grid[x][y] == '0':
            return 0
        if tuple(start) in self.visited:
            return 0 

        for new_x,new_y in [[0,1], [1,0], [0,-1], [-1,0]]:
            if 0 <= x + new_x < len(grid) and 0 <= y + new_y < len(grid[0]):
                self.visited.add(tuple(start))
                self.explore_island((x+new_x, y+ new_y), grid)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                res += self.explore_island((i, j), grid)

        return res
