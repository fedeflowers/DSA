"""
# Explanation of LeetCode Solution for "Valid Word Square"

## 1. Brief Explanation of the Approach
The problem "Valid Word Square" requires you to determine whether a list of words can be arranged to form a valid word square. A valid word square is an `N x N` array of characters such that the `i-th` row is the same as the `i-th` column for all valid indices.

The solution follows these steps:
- First, it calculates the length `n` of the input list `words`.
- Then, it iterates through each row (using index `i`).
- For each character in the current row (using index `j`), it performs three checks:
  1. **Row Length Check**: It ensures that the current column index `j` does not exceed the number of words `n`. If it does, it returns `False`.
  2. **Column Length Check**: It checks whether the row corresponding to the current column `j` has enough characters (i.e., `i` should be less than the length of `words[j]`). If not, it returns `False`.
  3. **Character Match Check**: It verifies that the character in the current row (`words[i][j]`) is the same as the character in the corresponding column (`words[j][i]`). If they differ, it returns `False`.
- If all checks are passed, then the function returns `True`, indicating the input forms a valid word square.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The algorithm runs in `O(n^2)` time complexity, where `n` is the number of words. This is because, in the worst case, we check each character in an `N x N` word square (which has size `n`).
  
- **Space Complexity**: 
  - The space complexity is `O(1)` since the algorithm uses only a fixed number of additional variables for counts and indices, and does not require any extra data structures that scale with input size.

## 3. Why This Approach is Efficient
This approach is efficient for the following reasons:
- It avoids unnecessary checks and only iterates through the matrix of characters that need to be validated.
- By performing inline checks, the function processes the data in a single pass through the word square, thus minimizing the number of operations.
- The checks are straightforward and require simple index comparisons and character comparisons, ensuring a quick response for small to moderate sizes of input.

Overall, the solution is both time-efficient and straightforward, making it suitable for the constraints typically seen in competitive programming problems like these.

Runtime: undefined
Memory: 19864000
"""

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            row = words[i]
            for j in range(len(row)):               
                if j >= n:
                    return False
                if i >= len(words[j]):
                    return False
                if row[j] != words[j][i]:
                    return False

        return True
