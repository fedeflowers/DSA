"""
# Explanation of the LeetCode Solution for "Number of Islands"

## 1. Approach Explanation

The solution employs a depth-first search (DFS) algorithm to traverse and explore each island in the given 2D grid. The grid consists of '1's (land) and '0's (water). The solution counts the number of distinct islands by following these steps:

- **Initialization**: A set called `visited` is used to keep track of cells that have already been explored to avoid counting them multiple times.

- **Explore Island**: The method `explore_island` takes a starting cell (coordinates) and the grid as parameters. It performs the following:
  - If the current cell is water ('0'), it returns `0` indicating that no island is found.
  - If the current cell has already been visited, it also returns `0` to avoid redundant exploration.
  - If the current cell is part of an island ('1'), the method explores its adjacent cells (right, down, left, up) recursively using a loop. Before making a recursive call, the current cell is marked as visited.
  
- **Count Islands**: The method `numIslands` iterates through each cell in the grid. For each cell, it calls `explore_island`. Each successful call that marks an island as visited increments a counter (`res`). The final count of islands is returned.

## 2. Time and Space Complexity Analysis

### Time Complexity
- **O(N)**: Here, `N` is the total number of cells (rows * columns) in the grid. Each cell is visited at most once during the DFS, leading to a linear time complexity relative to the number of cells in the grid.

### Space Complexity
- **O(N)**: The space complexity is primarily due to the `visited` set which stores each visited cell. In the worst case (when the entire grid is an island), the depth of the recursive stack can also grow, which can be O(N) for the call stack space.

## 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Direct Exploration**: The DFS allows for direct exploration of connected land cells with minimal overhead. Each cell is processed at most once, leading to an optimal traversal of the grid.

- **No Auxiliary Structures**: The solution uses a single set to track visited nodes, minimizing additional memory usage beyond what is necessary for tracking visited states.

- **Simplicity and Clarity**: The recursive nature of the DFS simplifies the code structure, making it straightforward to follow the logic of visiting connected components (islands).

Overall, this method effectively utilizes DFS to explore the grid systematically while ensuring that each cell contributes to the island count accurately.

Runtime: undefined
Memory: 26316000
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
