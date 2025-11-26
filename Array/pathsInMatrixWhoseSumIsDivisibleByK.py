"""
```markdown
# Explanation of the Solution for "Paths in Matrix Whose Sum Is Divisible by K"

## 1. Approach Explanation
The problem requires finding the number of distinct paths from the top-left corner of a grid to the bottom-right corner such that the sum of the values along the path is divisible by a given integer \( k \). 

The solution employs dynamic programming (DP) to keep track of the number of ways to reach each cell in the grid while keeping track of the modulo \( k \) of the sum of the path values.

### Key Steps:
- **DP Structure**: 
    - A 3D list `dp[i][j][r]`, where \( i \) and \( j \) are the coordinates of the grid, and \( r \) is the remainder when the sum of the path values modulo \( k \). `dp[i][j][r]` represents the count of paths to cell (i, j) with a sum that gives a remainder \( r \) when divided by \( k \).

- **Initialization**:
    - Start by initializing `dp[0][0][grid[0][0] % k] = 1`, since there’s one path to the starting cell with its value modulo \( k \).

- **State Transition**:
    - For each cell `(i, j)`, iterate through all possible remainders \( r \) (from \( 0 \) to \( k-1 \)):
        - Calculate `new_r`, which is the new remainder after adding the current cell value `grid[i][j]` to the previous remainder \( r \).
        - Update paths from the top neighbor `(i-1, j)` if it exists, and from the left neighbor `(i, j-1)` if it exists.
        - Take care to update the counts modulo \( MOD \) to prevent overflow.

- **Final Count**:
    - The result is found in `dp[n-1][m-1][0]`, which counts the number of paths that end at the bottom-right corner with a sum that is divisible by \( k \).

## 2. Time and Space Complexity Analysis
- **Time Complexity**: 
    - The solution consists of three nested loops:
        - Outer loops iterate over \( n \) (rows) and \( m \) (columns), contributing \( O(n * m) \).
        - The innermost loop iterates over \( k \), contributing \( O(k) \).
    - Thus, the overall time complexity is \( O(n * m * k) \).

- **Space Complexity**: 
    - A 3D list `dp` is created of dimensions \( n \times m \times k \).
    - Therefore, the space complexity is \( O(n * m * k) \).

## 3. Why This Approach is Efficient
- **Dynamic Programming** enables us to break down the problem into manageable subproblems by reusing previously computed results for paths ending at prior cells, thus avoiding recalculating path sums redundantly.
- By tracking the count of paths that yield different remainders modulo \( k \), we efficiently handle the divisibility condition without having to explore all path combinations exhaustively, which would be computationally prohibitive.
- The use of modular arithmetic ensures that numerical values remain manageable, adhering to the problem's requirements regarding large numbers.

This structured approach provides a robust solution to the problem while managing time and space effectively.
```

Runtime: undefined
Memory: 98392000
"""

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        n, m = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(n):
            for j in range(m):
                for r in range(k):
                    new_r = (r + grid[i][j]) % k # non so da quale remainder arrivo quindi lo calcolo per ciascuno
                    if i > 0:
                        dp[i][j][new_r] = (dp[i-1][j][r] + dp[i][j][new_r]) % MOD
                    if j > 0:
                        dp[i][j][new_r] = (dp[i][j-1][r] + dp[i][j][new_r]) % MOD

        return dp[-1][-1][0]
