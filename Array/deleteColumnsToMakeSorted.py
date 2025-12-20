"""
# Explanation of the LeetCode Solution for "Delete Columns to Make Sorted"

## 1. Brief Explanation of the Approach

The problem "Delete Columns to Make Sorted" requires determining how many columns in a given list of strings need to be deleted to ensure that the remaining columns are sorted in lexicographical order. 

The provided code takes the following approach:

- It initializes a counter `cols_to_delete` to zero, which tracks the number of columns that need to be deleted.
- It then iterates over each column of the first string (assuming that all strings are of the same length).
- For each character in the column, it compares it with the corresponding character in the previous string. If the current character is less than the previous one (i.e., violates the sorted order), it increments the `cols_to_delete` counter and breaks the inner loop to proceed to the next column.
- The loop continues until all columns are processed, after which it returns the total number of columns that need to be deleted.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N * M)
  - Where N is the number of strings and M is the length of each string. The outer loop iterates over each character (column) in the strings, and the inner loop iterates through all the strings to compare the characters in the current column.

- **Space Complexity**: O(1)
  - The solution uses a constant amount of extra space for variables like `cols_to_delete` and `prev`, regardless of the size of the input.

## 3. Why this Approach is Efficient

This approach is efficient for the following reasons:

- **Direct Comparison**: By directly comparing adjacent characters in the current column across all strings, the solution efficiently identifies violations of the sorting requirement.
- **Early Break**: The use of a `break` statement in the inner loop allows the algorithm to stop evaluating further strings for a column as soon as a violation is found, which can save unnecessary comparisons.
- **Simplicity**: The implementation is straightforward, making it easy to understand and debug. It systematically assesses each column independently, ensuring that the logic is clean and avoids unnecessary complexity.

In conclusion, this solution effectively balances clarity and performance, making it both an optimal and an elegant solution to the problem.

Runtime: undefined
Memory: 18264000
"""

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs: return 0
        cols_to_delete = 0
        for curr_col in range(len(strs[0])):
            prev = None
            for s in strs:
                if prev and prev > s[curr_col]:
                    cols_to_delete += 1
                    break
                prev = s[curr_col]

        return cols_to_delete


