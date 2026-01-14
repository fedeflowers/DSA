"""
```markdown
# Explanation of the "Number of Islands" Solution

## 1. Approach Explanation

The solution employs Depth-First Search (DFS) to explore and count the number of islands ('1's) in the given 2D grid which represents land and water. The method `numIslands` iterates through each cell of the grid:

- When it encounters a '1', it calls the `explore_island` function to explore the entire island, marking visited cells to prevent counting the same island multiple times. 
- The `explore_island` function performs the following:
    - Checks if the current cell is water ('0') or already visited; if so, it returns 0 (not part of an island).
    - For each of the four possible directions (up, down, left, right), it invokes itself recursively to continue exploring adjacent land cells.
    - After all adjacent land cells for a given island have been visited, it returns 1 to signify that one island has been counted.

The final count of islands is maintained in the `res` variable, which is returned as the output.

## 2. Time and Space Complexity Analysis

- **Time Complexity:** O(N), where N is the number of cells in the grid. In the worst case, each cell will be visited once, leading to a linear time complexity relative to the number of cells.
  
- **Space Complexity:** O(N) due to the use of the `visited` set which potentially holds every cell in the grid if all cells are part of islands. Additionally, the maximum depth of the recursion stack could also go up to O(N) in the worst case.

## 3. Efficiency of the Approach

This DFS approach is efficient for the following reasons:

- **Exhaustive Search:** The algorithm ensures that every part of an island is explored fully, which guarantees an accurate count of islands.
- **In-Place Travel:** By using a set to track visited cells, it avoids revisiting cells and ensures that operations are only performed on unvisited cells.
- **Simplicity of Implementation:** The recursive DFS is relatively simple to implement and understand, allowing for elegant traversal of the grid without the need for complex data structures or algorithms.

Overall, this method is both effective and intuitive for solving the problem of counting islands in a grid.
```

Runtime: undefined
Memory: 26308000
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
