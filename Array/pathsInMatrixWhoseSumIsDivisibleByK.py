"""
## Solution Explanation for "Paths in Matrix Whose Sum Is Divisible by K"

### 1. Brief Explanation of the Approach
The solution uses dynamic programming to count the number of paths in a matrix where the sum of the path's elements is divisible by a given integer \( k \).

- **Data Structure**: A 3D list `dp` is utilized where `dp[i][j][r]` indicates how many unique paths exist to the cell `(i, j)` such that the sum of the elements along the path from the top-left corner `(0, 0)` to `(i, j)` has a remainder \( r \) when divided by \( k \).

- **Initialization**: The starting point `dp[0][0][grid[0][0] % k]` is initialized to `1` since there is one way to start at the grid's origin with its respective sum.

- **Building the DP Table**: The algorithm iterates over each cell in the matrix. For each position `(i, j)`, it checks the paths coming from the cell above `(i-1, j)` and the cell to the left `(i, j-1)`. For each valid path taken from these positions, the new potential remainder when adding the current cell's value is calculated. The corresponding counts of paths leading to `new_r` are updated.

- **Result**: Finally, it returns the number of paths to the bottom-right corner `(m-1, n-1)` that yield a sum divisible by \( k \) (i.e., remainder `0`).

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The algorithm processes each cell in the `m x n` grid and checks each of the \( k \) remainders. Thus, the time complexity is \( O(m \times n \times k) \).

- **Space Complexity**: The space complexity is determined by the 3D list `dp`, which contains \( m \times n \times k \) elements. Hence, the space complexity is also \( O(m \times n \times k) \).

### 3. Why This Approach Is Efficient
This approach is efficient given the constraints typically associated with matrix and path sum problems:

- **Utilization of Remainders**: By focusing on remainders instead of directly storing sums, we can potentially reduce the state space significantly. Instead of tracking all possible sums, we only track \( k \) possible remainders, which leads to improved space and time efficiency in situations where \( k \) is relatively small compared to the sum of elements.

- **Comprehensive Path Counting**: The algorithm efficiently counts paths through its dynamic programming formulation, allowing for the reuse of previously computed results (optimal substructure), which is a fundamental principle of DP.

- **Iterative Filling**: The iterative filling of the DP table allows for systematic accumulation of path counts, ensuring all potential routes to each cell are considered without redundant calculations or recursion overhead.

Overall, this method balances comprehensiveness with efficiency, making it suitable for larger matrices, particularly when \( k \) is small.

Runtime: undefined
Memory: 98372000
"""

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for r in range(k):
                    if i > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i-1][j][r]) % MOD
                    if j > 0:
                        new_r = (r + grid[i][j]) % k
                        dp[i][j][new_r] = (dp[i][j][new_r] + dp[i][j-1][r]) % MOD

        return dp[m-1][n-1][0]
        
