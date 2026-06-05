"""
```markdown
## Explanation of LeetCode Solution: "Find the Index of the First Occurrence in a String"

### 1. Brief Explanation of the Approach
The problem requires finding the first occurrence of the substring (needle) within a larger string (haystack). The provided solution employs a straightforward approach using nested loops:

- The outer loop iterates through each index of the haystack string.
- For each starting index `i` in haystack, the inner loop checks if the substring starting from `i` matches the needle.
- The `while` loop increments index `j` if the characters of `haystack` and `needle` match.
- If the entire needle is matched (i.e., the length of matched characters equals the length of the needle), the function returns the starting index `i`.
- If no match is found after checking all potential starting indices in the haystack, the function returns `-1`.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The worst-case time complexity is \(O(N \times M)\), where:
  - \(N\) is the length of the haystack, and
  - \(M\) is the length of the needle.
  
  In the worst scenario, we might need to check every possible starting position in haystack and, for each position, compare all characters of needle.

- **Space Complexity**: The space complexity is \(O(1)\) because the solution uses a fixed amount of extra space regardless of input size (only a few integer variables are used).

### 3. Why This Approach is Efficient
Although the provided solution works correctly and is easy to understand, it can be inefficient for large strings due to its \(O(N \times M)\) time complexity. Major reasons for efficiency include:

- **Simplicity**: The solution's logic is straightforward, making it easy to read and understand.
- **Early Exit**: The check `len(haystack) - i >= len(needle)` ensures that unnecessary comparisons are avoided if the remaining part of the haystack is shorter than the needle.
- **Direct Comparison**: It compares characters directly without the need for additional data structures; it uses indices to keep track of currently processed positions.

However, there are more advanced algorithms available, like the Knuth-Morris-Pratt (KMP) algorithm, which can solve this problem in linear time \(O(N + M)\). Those would generally be preferred in scenarios where performance is critical.
```

Runtime: N/A
Memory: N/A
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            j = i
            if len(haystack) - i >= len(needle):
                while j-i < len(needle) and haystack[j] == needle[j-i]:
                    j += 1
                if j - i == len(needle):
                    return i

        return -1
