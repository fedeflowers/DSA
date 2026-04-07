"""
```markdown
## Minimum Window Substring Solution Explanation

### 1. Brief Explanation of the Approach

The solution employs the **sliding window** technique to find the minimum window substring of `s` that contains all the characters of `t`. Here's a step-by-step breakdown of the approach:

- **Character Count**: A dictionary (`ref`) tracks the frequency of each character in string `t`. This will help determine the characters that need to be included in the window.
  
- **Window Expansion**: A variable `end` loops through the string `s`. For each character, if it's included in the `ref`, the algorithm checks if we still need it (i.e., if its count in `ref` is greater than zero). If we need it, we decrement `required` which tracks how many characters from `t` are still needed in the current window.
  
- **Window Contraction**: When `required` becomes zero, it indicates that the current window contains all the characters of `t`. The algorithm calculates the length of this window and stores it if it's smaller than the previously found smallest window. The algorithm then attempts to contract the window by moving the `start` pointer right, adjusting the counts accordingly and potentially increasing `required` again if characters are recaptured in the window.
  
- **Result**: The process continues until all characters of `s` have been considered, and the smallest valid window substring is returned.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N + M)
  - Here, N is the length of string `s`, and M is the length of string `t`. The algorithm processes each character of `s` and possibly each character of `t` within the nested loops, but overall terminates in linear time as each character is processed a constant number of times.
  
- **Space Complexity**: O(M)
  - The `ref` dictionary uses space proportional to the size of `t` in the worst case (if all characters are distinct), leading to O(M) space complexity.

### 3. Why This Approach is Efficient

This approach is efficient because it optimally narrows down and expands a window in a linear pass through the string due to the sliding window technique. Instead of exhaustively checking every possible substring of `s`, it directly works on maintaining a valid window that contains all required characters. Hence, it saves time and computational resources compared to straightforward substring checking methods, making it suitable for the problem at hand.
```

Runtime: undefined
Memory: 19700000
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = {}
        for c in t:
            ref[c] = ref.get(c, 0) + 1

        start = 0
        res = ""
        l_res = float("inf")
        required = sum(ref.values())  # total chars still needed

        for end in range(len(s)):
            if s[end] in ref:
                if ref[s[end]] > 0:   # only counts if we actually needed it
                    required -= 1
                ref[s[end]] -= 1

            while required == 0:
                window_len = end - start + 1
                if window_len < l_res:
                    l_res = window_len
                    res = s[start:end + 1]

                if s[start] in ref:
                    ref[s[start]] += 1
                    if ref[s[start]] > 0:  # only counts if we now need it again
                        required += 1
                start += 1

        return res
