"""
## Explanation of the Approach

The given solution for the "Special Binary String" problem utilizes a recursive strategy to construct the largest special binary string from the input string. Here’s a step-by-step breakdown of the approach:

1. **Identify Special Subsequences**: 
   - The special binary string is defined as a string that starts with '1', ends with '0', and contains the same number of '1's as '0's among its subparts. The algorithm scans through the input string `s` and keeps track of the balance between '1's and '0's using a `count` variable.
   - As we iterate through `s`, we increment `count` when we encounter '1' and decrement it for '0'. When `count` reaches zero, it indicates that we've found a valid special substring.

2. **Recursive Construction**: 
   - When a valid special substring is identified (from index `i` to `j`), it's split out, and the function is called recursively on the substring enclosed by this special substring (i.e., between `i+1` and `j`).
   - The recursive call results in potentially finding and forming new special strings from the inner substring, which is then wrapped by '1' and '0' to maintain the special substring structure.

3. **Sorting for Largest String**: 
   - The newly formed components are collected in a list `res`, which is then sorted in reverse order. Sorting ensures that when concatenated, the result represents the largest possible binary string.

4. **Final Output**: 
   - The sorted parts are then combined and returned as the final result.

## Time and Space Complexity Analysis

- **Time Complexity**: 
  The worst-case time complexity can be analyzed as follows:
  - The function iterates through the string `s` in a linear manner. For each special substring found, it recursively processes a shorter substring, leading to a depth proportional to the number of '1's (which is about half the length of the string).
  - Each time we split and process substrings, the operation requires O(N log N) time due to sorting, where N is the average length of the strings being processed. 
  - Therefore, the overall time complexity can be approximated as O(N log N), where N is the length of the input string.

- **Space Complexity**: 
  The primary space usage comes from:
  - The list `res` which stores the valid special substrings. In the worst case (when the string may contain many special substrings), this could require up to O(N) space for storage.
  - The recursive calls can also use stack space proportional to the depth of recursion. Thus, the overall space complexity can be considered O(N) due to the storage of results and recursive call stack.

## Why This Approach is Efficient

1. **Forethought in Special Binary Structures**: 
   Recognizing and efficiently identifying special substrings ensures that we are building the largest possible outcome in each recursive step. By ensuring that we only consider valid segments of the original string, we avoid unnecessary processing and minimize redundant computations.

2. **Sorting Strategy**: 
   The use of sorting immediately at each level of recursion allows the algorithm to directly build the largest possible result, guaranteeing that the final output is optimal without needing further adjustments.

3. **Recursive Decomposition**: 
   The approach effectively breaks down the problem into smaller, manageable parts, leveraging recursion to handle complexity while staying within the constraints of the definition of a special binary string.

Overall, the combination of careful structuring of the input and strategic recursive handling of substrings leads to an efficient solution that consistently forms the desired large special binary string.

Runtime: undefined
Memory: 19356000
"""

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # find valid substrings, split and reorder
        res = []
        i = 0
        count = 0
        for j in range(len(s)):
            count += 1 if s[j] == '1' else -1
            if count == 0: #found special bin string
                #split
                res.append("1" + self.makeLargestSpecial(s[i+1: j]) + "0")
                i = j + 1

        res.sort(reverse=True)
        return "".join(res)
