"""
```markdown
# Explanation of the LeetCode Solution for "Minimum ASCII Delete Sum for Two Strings"

## 1. Brief Explanation of the Approach

The problem "Minimum ASCII Delete Sum for Two Strings" requires finding the minimum ASCII value of characters that must be deleted from two strings to make them equal. This solution uses dynamic programming to build a 2D table (`dp`) that helps compute the minimum deletion cost iteratively.

Here’s a step-by-step breakdown of the approach:

- **Initialization**: Create a 2D array `dp` of size `(m + 1) x (n + 1)`, where `m` and `n` are the lengths of the input strings `s1` and `s2`. The value `dp[i][j]` will represent the minimum ASCII deletion sum needed to make the first `i` characters of `s1` and the first `j` characters of `s2` equal.

- **Base Cases**:
  - The first column (`dp[i][0]`) is filled to represent the cost of converting the first `i` characters of `s1` to an empty string (i.e., summing the ASCII values of those characters).
  - The first row (`dp[0][j]`) represents converting an empty string to the first `j` characters of `s2`.

- **Filling the DP Table**:
  - For each character position `(i, j)`, if `s1[i - 1]` equals `s2[j - 1]`, then no deletion is required, thus `dp[i][j]` is taken from `dp[i - 1][j - 1]`.
  - Otherwise, calculate the minimum of either deleting the current character from `s1` or from `s2`. The costs will be the previous states plus the ASCII value of the character being deleted.

- **Result**: The final answer, the minimum ASCII delete sum required to make the strings equal, is found in `dp[m][n]`.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of the solution is O(m * n), where `m` is the length of `s1` and `n` is the length of `s2`. This stems from the need to fill each entry of the `dp` table which has dimensions `(m + 1) x (n + 1)`.

- **Space Complexity**: The space complexity is O(m * n) as well, due to the storage requirement for the `dp` table.

## 3. Why This Approach is Efficient

This dynamic programming approach is efficient because:
- It systematically considers all possible cases for matching characters or performing deletions, ensuring that all possible solutions are explored without overlapping recalculations, which can occur in naive recursive solutions. 
- The bottom-up construction of the DP table utilizes previously computed results, leading to efficient computation of the final answer in polynomial time.
- By maintaining a 2D DP table, the solution is straightforward and easy to implement, while clearly exhibiting the relationships between subproblems.

In conclusion, this method is ideal for problems involving string manipulations and comparisons, where optimal substructure is present.
```

Runtime: undefined
Memory: 23624000
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Lengths of the input strings
        m, n = len(s1), len(s2)
        
        # Create a 2D DP array with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the first column: cost of deleting from s1 to empty
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        
        # Fill the first row: cost of deleting from s2 to empty
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        # Fill the rest of the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match, no deletion needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose the minimum cost between deleting from s1 or s2
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        
        # The answer is the value in the bottom-right corner of the dp table
        return dp[m][n]


