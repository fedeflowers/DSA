"""
## Explanation of the Solution for "Delete Columns to Make Sorted"

### 1. Brief Explanation of the Approach
The problem requires us to determine the minimum number of columns that need to be deleted from a list of strings such that the remaining columns are sorted in non-decreasing order. 

The approach used in the solution iterates over the columns of the input strings. For each column, it checks if the characters in that column are sorted in non-decreasing order. If it detects that any character in this column is greater than the character from the previous string (`prev`), it counts that column for deletion.

To achieve this, the solution uses:
- A loop to iterate over the columns of the strings.
- A nested loop to compare the elements of the current column across the strings.
- A variable `prev` to hold the previously compared character, starting from `None`.

If the current character (`s[curr_col]`) appears before the `prev` character in lexicographical order, it means the column is out of order and should be marked for deletion (incrementing the `cols_to_delete` counter).

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of this approach is \(O(N \times M)\), where:
  - \(N\) is the number of strings in the input list `strs`.
  - \(M\) is the length of each string (number of columns).
  
  The outer loop iterates through each of the columns (of which there are \(M\)), while the inner loop goes through each of the \(N\) strings to compare the characters in that column.
  
- **Space Complexity**: The space complexity is \(O(1)\) since we only use a constant amount of extra space to store the `cols_to_delete` counter and the `prev` variable.

### 3. Why This Approach is Efficient
This approach is efficient because:
- It directly checks the sorting condition on a column-by-column basis, which is clear and intuitive.
- The nested loops ensure that each element is compared exactly once, leading to a linear pass through the data for each column. Thus, the overall complexity scales linearly with the size of the input.
- Unlike the previous solution using `zip` and sorting, which has a complexity of \(O(M \times N \log N)\) due to the sorting operation, this solution avoids unnecessary computations by simply checking the order of characters, leading to better performance especially with larger data sets.

In summary, the solution is efficient in both time and space, making it suitable for the given problem constraints.

Runtime: undefined
Memory: 17900000
"""


# # $O(M \times N \log N)$)
# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         count = 0
#         for col in zip(*strs):
#             if list(col) != sorted(col):
#                 count += 1
#         return count

# O(N*M)
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

