"""
## Explanation of the LeetCode Solution for "Valid Word Abbreviation"

### 1. Approach Explanation
The solution uses two pointers, `i` for the `word` and `j` for the `abbr` (abbreviation) to traverse both strings simultaneously. The algorithm works as follows:

- Initialize two pointers `i` and `j` to 0 and get the lengths of `word` and `abbr`.
- Use a `while` loop to ensure we traverse both strings until either pointer reaches the end.
- Inside the loop:
  - If the character at `abbr[j]` is a digit, we extract the full number to determine how many characters should be skipped in `word`. 
    - If a leading zero is encountered, the abbreviation is invalid.
    - The number is constructed by multiplying the current value by 10 and adding the integer value of the current digit, incrementing `j` until we find a non-digit character.
  - If the character at `abbr[j]` is not a digit, then match it with the character at `word[i]`. If they don’t match, return `False`.
- After the loop, check if both pointers, `i` and `j`, have reached the ends of their respective strings. This confirms that the entire `word` matches the `abbr`. The function returns `True` if both pointers are at the end, otherwise, it returns `False`.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(m + n), where `m` is the length of `word` and `n` is the length of `abbr`. In the worst case, we traverse both strings entirely once.
- **Space Complexity**: O(1). The solution uses a constant amount of additional space (just a few variables) regardless of the input sizes.

### 3. Efficiency of the Approach
This approach is efficient for several reasons:
- **Single Pass**: It only requires a single pass through both strings, making it linear in terms of time complexity.
- **No Extra Structures**: It doesn’t require any additional data structures, which contributes to its constant space complexity.
- **Direct Mapping of Characters**: The solution effectively maps the digits to character skips, making it intuitive and straightforward to check if a string abbreviation is valid.
- **Validation of Leading Zeros**: It includes an early return for invalid cases (leading zero), ensuring we can terminate checks quickly in such scenarios without unnecessary processing.

Overall, the solution is well-optimized for the problem at hand and effectively checks the validity of the word abbreviation.

Runtime: undefined
Memory: 17968000
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if abbr[j].isdigit():
                # Leading zeros are invalid
                if abbr[j] == '0': 
                    return False
                
                # Parse the full number
                val = 0
                while j < n and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])
                    j += 1
                
                # Skip characters in word
                i += val
            else:
                # Match characters
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        # Both pointers must reach the end
        return i == m and j == n
