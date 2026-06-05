"""
```markdown
## Explanation of the Solution

### 1. Approach

The solution aims to find the index of the first occurrence of the substring `needle` within the string `haystack`. It utilizes a simple brute-force comparison method:

- The outer loop iterates over each character in `haystack` using an index `i`.
- Before comparing, it checks if there are enough characters remaining in `haystack` to potentially match `needle` (i.e., `len(haystack) - i >= len(needle)`).
- An inner loop compares characters from `haystack` starting at index `i` with characters from `needle`. The inner index `j` is incremented as long as the characters match and the length of matched characters does not exceed the length of `needle`.
- If the entire `needle` is matched (`j - i == len(needle)`), the function returns the starting index `i`.
- If no match is found after completing the iterations, the function returns -1.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N * M) in the worst case, where N is the length of `haystack` and M is the length of `needle`. In the worst-case scenario, it iterates through `haystack` and for each position, it may potentially check all characters of `needle`.
  
- **Space Complexity**: O(1) since it only uses a fixed amount of extra space for variables `i` and `j`, regardless of the input size.

### 3. Efficiency of the Approach

While this solution is straightforward and easy to understand, its efficiency can be improved. However, for small strings or simple use cases, this brute-force technique is acceptable. The key benefits include:

- **Simplicity**: The implementation is straightforward, making it easy to understand and maintain.
- **No Extra Data Structures**: It doesn't use additional data structures, keeping the memory footprint low, which can be advantageous in certain environments.

However, for larger inputs or performance-critical applications, more efficient algorithms (like the Knuth-Morris-Pratt or Rabin-Karp algorithms) are recommended to reduce the time complexity significantly.
```

Runtime: undefined
Memory: 19236000
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
