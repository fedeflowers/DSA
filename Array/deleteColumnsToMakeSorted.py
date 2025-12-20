"""
## Explanation of the Approach

The solution to the problem "Delete Columns to Make Sorted" utilizes the idea of comparing each column of characters formed from the input list of strings. The goal is to determine how many columns do not remain sorted when assessed from top to bottom.

### Detailed Steps:
1. **Transposing the Column**: The built-in `zip(*strs)` technique effectively groups characters based on their column positions across all strings. Each resulting tuple represents a column of characters.
  
2. **Sorting Check**: For each column (as a tuple), the solution checks if the column matches its sorted version. If the column is not sorted (i.e., `list(col) != sorted(col)`), we increment a counter `count`.

3. **Returning the Result**: Finally, the total count of unsorted columns is returned.

## Time and Space Complexity Analysis

### Time Complexity:
- Let `N` be the number of strings and `M` be the length of each string.
- The solution iterates over `M` columns, and for each column, it converts the tuple into a list and checks if it is sorted. This sorting check takes O(N log N) since `sorted` is used, leading to an overall time complexity of:
  \[
  O(M \cdot N \log N)
  \]

### Space Complexity:
- The space complexity is primarily due to the tuples created by `zip`. Since we create a separate list for each column, the space complexity can be expressed as O(N) — for storing characters in each tuple (since the tuple length is confined to the number of strings). Therefore, the overall space complexity is O(N).

## Why This Approach is Efficient

1. **Simplicity**: The approach leverages Python's built-in functions like `zip` and `sorted`, which are optimized and make the code concise and easy to read.

2. **Direct Comparison**: Instead of managing a manual comparison and condition checks as in the first implementation, this approach directly compares the column contents against their sorted counterpart, effectively minimizing the complexity of the code.

3. **Efficiency**: While the time complexity involves sorting, this is acceptable because the problem size is typically manageable, especially in competitive programming scenarios where N and M are limited.

In summary, this code is efficient due to its direct and simple checking method, making it both effective and readable.

Runtime: undefined
Memory: 18112000
"""

# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         if not strs: return 0
#         cols_to_delete = 0
#         for curr_col in range(len(strs[0])):
#             prev = None
#             for s in strs:
#                 if prev and prev > s[curr_col]:
#                     cols_to_delete += 1
#                     break
#                 prev = s[curr_col]

#         return cols_to_delete


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                count += 1
        return count

