"""
```markdown
# Explanation of LeetCode Solution for "Minimum ASCII Delete Sum for Two Strings"

## 1. Brief Explanation of the Approach

The problem "Minimum ASCII Delete Sum for Two Strings" asks us to find the minimum sum of ASCII values of characters that need to be deleted from two strings to make them equal. 

The approach used in the provided solution employs dynamic programming (DP) to build a solution incrementally. Here's a walkthrough of the algorithm:

- **DP Table Initialization**: We initialize a 2D list `dp` where `dp[i][j]` represents the minimum delete sum required to make the first `i` characters of `s2` and the first `j` characters of `s1` equal.

- **Base Cases**:
  - For an empty `s2` (i.e., `i = 0`), the cost to delete all characters from `s1` to make it equal to `s2` is the sum of ASCII values of all characters in `s1`.
  - For an empty `s1` (i.e., `j = 0`), the cost to delete all characters from `s2` is the sum of ASCII values of all characters in `s2`.

- **Filling the DP Table**:
  - For every character pair `(s2[i-1], s1[j-1])`, we have two scenarios:
    - If the characters are equal, `dp[i][j]` takes the value from `dp[i-1][j-1]`, which means no deletion is needed.
    - If they are not equal, we take the minimum value between:
      - Deleting the character from `s2` (`dp[i-1][j] + ord(s2[i-1])`)
      - Deleting the character from `s1` (`dp[i][j-1] + ord(s1[j-1])`)

- **Final Result**: The answer will be stored in `dp[l2][l1]`, representing the minimum delete sum for the entire strings.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(N * M), where N is the length of `s2` and M is the length of `s1`. This is due to the nested loop structure used to fill in the DP table, iterating through each pair of characters from both strings.

- **Space Complexity**: The space complexity is O(N * M) as well, because we are using a 2D list to store the DP results. If we optimize the space using a single-dimensional array, we can reduce the space required.

## 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Dynamic Programming**: It breaks down the problem into smaller subproblems that are solved independently and stored, preventing redundant calculations. This is the essence of dynamic programming and helps with both optimal substructure and overlapping subproblems.

- **Iterative Solution**: By filling the DP table iteratively, it avoids the pitfalls of recursion which can lead to stack overflow on large inputs and may have poor performance due to repeated calculations.

- **Clear Problem Decomposition**: The algorithm clearly defines how to handle equal and unequal characters and captures the essence of the problem by calculating the minimum delete cost, thus ensuring an accurate and efficient approach.

In conclusion, the solution is efficient, maintains clarity, and scales well with larger inputs due to the structured nature of the dynamic programming technique.
```

Runtime: undefined
Memory: 23760000
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)

        dp = [[0] * (l1+1) for _ in range(l2+1)]

        #init
        for j in range(1, l1+1):
            dp[0][j] = dp[0][j-1] + ord(s1[j-1])
        for i in range(1, l2+1):
            dp[i][0] = dp[i-1][0] + ord(s2[i-1])


        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if s1[j-1] == s2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s2[i-1]), dp[i][j-1] + ord(s1[j-1])) 

        return dp[-1][-1]

