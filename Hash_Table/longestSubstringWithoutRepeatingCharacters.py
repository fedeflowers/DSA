"""
```markdown
## Solution Explanation for "Longest Substring Without Repeating Characters"

### 1. Approach Explanation
The solution uses a sliding window technique to find the length of the longest substring that can be formed without repeating characters. Here’s how the algorithm works step-by-step:

- **Initialization**: Start with two pointers - `l` (left) and `r` (right), which denote the current window of the substring. `chars` is a dictionary to keep track of the frequency of characters in the current substring, and `max_l` is used to store the maximum length of a substring found so far.

- **Iteration**: Loop through the string with the right pointer `r`:
  - For each character at position `r`, increase its count in the `chars` dictionary.
  - If the character count in `chars` indicates this character has appeared more than once (`chars[s[r]] >= 2`), we have a repeat in the substring.
    - In this case, shift the left pointer `l` to the right until the substring becomes valid again (i.e., all characters in the current substring are unique). This is done by decreasing the count of the character at the left pointer and removing it from the dictionary if its count drops to zero.
    
- **Update Maximum Length**: After adjusting the window for any duplicates, update the maximum length found by checking the size of the current dictionary.

- **Return Result**: The final value of `max_l` contains the length of the longest substring without repeating characters.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the input string `s`. Each character is processed at most twice (once by the right pointer and once by the left pointer), resulting in a linear time complexity.

- **Space Complexity**: O(min(N, M)), where M is the size of the character set. Since we store the frequency of characters in a dictionary, in the worst case (if all characters are unique), we would store them all, leading to space complexity proportional to the size of the character set or the length of the string, whichever is smaller.

### 3. Efficiency of the Approach
This approach is efficient due to the sliding window technique, allowing us to traverse the string with minimal operations. This means that:

- We avoid nested loops, which typically result in O(N^2) time complexities. Instead, with a single pass through the string, the algorithm efficiently maintains a count of characters.
- The use of a dictionary allows for O(1) average-time complexity for insertions and lookups, making it quick to check for duplicates and maintain the sliding window.
- Overall, this ensures the solution is both time-efficient and space-efficient while solving the problem correctly.

```

Runtime: undefined
Memory: 19288000
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = {}
        max_l = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            while chars[s[r]] >= 2:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l+= 1
            max_l = max(max_l, len(chars))
        return max_l
