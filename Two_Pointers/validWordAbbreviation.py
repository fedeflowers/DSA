"""
```markdown
## Explanation of the Solution for "Valid Word Abbreviation"

### 1. Approach Explanation

The problem requires checking if a given abbreviation (abbr) can represent a specific word (word) according to certain rules. The abbreviation can contain letters corresponding to characters in the word and digits representing consecutive characters skipped. 

**Step-by-Step Breakdown:**

- Two pointers `i` and `j` are initialized to zero, which will traverse the `abbr` and `word` respectively.
- A while loop iterates until either the abbreviation (`abbr`) or the word (`word`) has been fully processed (i.e., until either pointer reaches the end of the respective string).
  - If the current character in `abbr` (`abbr[i]`) is a digit, it indicates the number of characters to skip in the `word`. If the digit is `0`, the abbreviation is invalid (since we can't skip 0 characters).
    - A loop accumulates the full number from the digits (e.g., "12" will be treated as 12, not as separate digits).
    - The pointer `j` is then advanced by that accumulated number.
  - If `abbr[i]` is a letter, it must match the current character in `word` (`word[j]`). If it doesn't match, the abbreviation is deemed invalid.
    - Both pointers are incremented by one.
- After exiting the loop, the function checks if both pointers have reached the end of their respective strings. If they have, it means the abbreviation is valid, and the function returns `True`. Otherwise, it returns `False`.

### 2. Time and Space Complexity Analysis

- **Time Complexity:** O(N + M), where N is the length of `abbr` and M is the length of `word`. Each character in both strings is processed at most once, leading to a linear time complexity in relation to the combined lengths of the two strings.
  
- **Space Complexity:** O(1). The solution uses a constant amount of extra space, with only a few integer variables to keep track of the pointers, resulting in a space complexity independent of the input size.

### 3. Efficiency of the Approach

This approach is efficient due to:

- **Single Pass:** The use of two pointers allows the solution to traverse the strings in a single pass without the need for additional data structures, making it optimal for time complexity.
- **Direct Character Matching:** Instead of generating all possible interpretations of the abbreviation, the approach directly compares characters, avoiding unnecessary computations or checks.
- **Handling Digits:** The approach effectively handles multiple digits and ensures proper parsing of numbers (like "12"), which is a common edge case in abbreviation problems.
  
Overall, its linear time complexity and constant space consumption make this solution suitable for situations with larger strings where efficiency is critical.
```

Runtime: undefined
Memory: 19568000
"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                num = 0
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                j += num
            else:
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
        return i == len(abbr) and j == len(word)
