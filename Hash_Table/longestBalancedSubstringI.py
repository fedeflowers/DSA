"""
```markdown
# Explanation of LeetCode Solution for "Longest Balanced Substring I"

## 1. Approach Explanation

The solution aims to find the length of the longest balanced substring from a given string `s`. A balanced substring is defined as a substring where all characters have the same frequency.

The approach involves using a nested loop to examine all possible substrings of the input string `s`. For each starting index `start`, the solution counts the frequencies of characters in the substring that extends from `start` to every possible ending index `end`.

- The outer loop iterates over each possible starting index `start`.
- The inner loop iterates over all possible ending indices `end`, from `start` to the end of the string `n`.
- A `defaultdict` is used to maintain the frequency count of characters within the current substring.
- For each substring, it converts the frequency values into a set. A substring is deemed balanced if this set contains only one unique value (i.e., all character frequencies are the same).
- If a balanced substring is found, the length is calculated and compared with the current maximum length (`max_length`), updating it if necessary.
- Finally, the function returns `max_length`, which represents the length of the longest balanced substring.

## 2. Time and Space Complexity Analysis

### Time Complexity
The time complexity of this solution can be analyzed by considering the nested loops:
- The outer loop runs for each character in the string, yielding `O(n)`.
- The inner loop also runs for each character starting from `start`, leading to a worst-case situation of approximately `O(n)` iterations for each of the outer loop iterations.

Thus, the overall time complexity is:
- `O(n^2)` for the nested loops, considering that checking the frequencies and converting them into a set takes O(1) time since the alphabet size is limited.

### Space Complexity
The space complexity is largely driven by the `defaultdict` used for character frequency counting:
- In the worst case, where all characters in the substring are unique, the space complexity can reach `O(k)` where `k` is the number of unique characters encountered in the current substring, but since `k` is also bounded by the alphabet size, it becomes constant in practical scenarios (O(1)).

Therefore, the overall space complexity is:
- `O(1)` since it does not scale with the input size in a practical sense.

## 3. Efficiency of the Approach

The approach efficiently explores all possible substrings with a combinatorial nature within a manageable time complexity of `O(n^2)`. While this may seem inefficient for longer strings, it effectively handles cases where the string length is moderate since it systematically checks each starting point and gradually expands the substring while maintaining a count of frequencies.

However, it's important to note that the method could be inefficient for particularly long strings due to quadratic time complexity. More optimal approaches (such as using two pointers or counting mechanisms) might exist for larger inputs, especially in competitive programming scenarios. Still, this method's simplicity and clarity make it a good learning example of substring handling and frequency counting.
```

Runtime: N/A
Memory: N/A
"""

class Solution:
    def longestBalanced(self, s: str) -> int:
        max_length = 0
        n = len(s)

        for start in range(n):
            frequency = defaultdict(int)
            for end in range(start, n):
                frequency[s[end]] += 1
                freq_values = set(frequency.values())
                if len(freq_values) == 1:
                    max_length = max(max_length, end - start + 1)

        return max_length 

