"""
```markdown
## Explanation of the Solution for "Magic Squares In Grid" on LeetCode

### 1. Brief Explanation of the Approach
The solution aims to count how many 3x3 magic squares exist within a given 2D grid of integers. A 3x3 magic square has the following properties:
- It consists of all unique numbers from 1 to 9.
- The sum of each row, column, and both diagonals equals 15.

The approach involves:
- Iterating through the grid to identify possible top-left corners of 3x3 subgrids.
- For each potential subgrid, checking whether the center of the square is 5 (a necessary condition for a 3x3 magic square).
- If the center is 5, further validating the properties of a magic square by:
  - Checking if it contains all numbers from 1 to 9.
  - Checking the sums of its rows, columns, and diagonals.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N * M), where N is the number of rows and M is the number of columns in the grid. The algorithm iterates through potential top-left corners of 3x3 subgrids, and for each subgrid, it performs a constant amount of work (checking sums and uniqueness, which operates in constant time since it's always 9 elements).
  
- **Space Complexity**: O(1) for auxiliary space since the solution primarily uses a fixed number of variables and does not require additional space that scales with input size.

### 3. Why This Approach is Efficient
The approach is efficient due to:
- **Early Pruning with Center Check**: It checks if the center of the 3x3 subgrid is 5 before performing further checks. This significantly reduces the number of unnecessary checks since only a configuration with a center of 5 can potentially be a magic square.
- **Constant Time Checks for Properties**: Validating whether the numbers are unique and if the sums match is done in constant time for each subgrid, keeping the iterations manageable.
- **Localized Operations**: The focus on 3x3 regions ensures that we are always working with a small and fixed number of elements, making both checks and iterations faster compared to a brute-force approach across larger sections of the grid.

Overall, the algorithm balances comprehensive checks with strategic early exits, making it both effective and efficient.
```

Runtime: undefined
Memory: 19268000
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_magic(r, c):
            # Check unique numbers 1-9
            vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False
            
            # Check rows, columns, and diagonals sum to 15
            # Row sums
            if any(sum(grid[r+i][c:c+3]) != 15 for i in range(3)):
                return False
            # Column sums
            if any(grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j] != 15 for j in range(3)):
                return False
            # Diagonals
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
            
            return True

        for r in range(rows - 2):
            for c in range(cols - 2):
                # Optimization: center of a 3x3 magic square must be 5
                if grid[r+1][c+1] == 5 and is_magic(r, c):
                    count += 1
        return count
