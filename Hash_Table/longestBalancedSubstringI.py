"""
# Explanation of LeetCode Solution for "Longest Balanced Substring I"

## 1. Brief Explanation of the Approach

The problem asks to find the length of the longest balanced substring in a given string `s`. A balanced substring is defined as one where all characters occur the same number of times.

The solution uses a nested loop structure to examine all possible substrings of the given string. The outer loop iterates over every possible starting index (`start`) of the substring, while the inner loop iterates over every possible ending index (`end`) that extends from the current starting index.

1. For each substring defined by `start` and `end`, a frequency dictionary counts how many times each character appears.
2. The set of values from the frequency dictionary is checked to see if all characters have the same frequency, meaning the length of the set should be 1 (i.e., all characters appear a uniform number of times).
3. If this condition is met, the length of the current substring (`end - start + 1`) is compared to `max_length` to potentially update it.

Finally, the function returns the length of the longest balanced substring found.

## 2. Time and Space Complexity Analysis

**Time Complexity:**
- The outer loop runs `n` times (for each starting index).
- The inner loop also can run up to `n` times in the worst case (for each ending index). 
- Checking the frequency dictionary involves traversing through the characters in the current substring, which can be up to `n`. 
- Therefore, the worst-case time complexity of this approach is **O(n^3)**.

**Space Complexity:**
- The space complexity is mainly determined by the frequency dictionary, which can store at most `k` unique characters (where `k` is the number of different characters in the string).
- Hence, the space complexity is **O(k)**.

## 3. Why This Approach is Efficient

Although the time complexity is on the higher side (`O(n^3)`), the approach is straightforward and easy to understand. This brute-force method guarantees finding the longest balanced substring by examining every possible substring in the given string `s`.

However, this approach is not efficient for large strings due to its cubic time complexity. For practical limits, optimizing the approach may be necessary, potentially moving to an alternative solution using a sliding window or hashing technique that avoids the full enumeration of substrings, reducing the time complexity significantly closer to linear or quadratic.

In its current form, while the provided solution works correctly to find the balanced substring, it may not perform well for larger input sizes typical for competitive programming contests or real-world applications.

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

