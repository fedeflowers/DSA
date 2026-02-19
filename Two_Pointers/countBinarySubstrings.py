"""
# Explanation of LeetCode Solution: "Count Binary Substrings"

## 1. Brief Explanation of the Approach

The problem "Count Binary Substrings" requires us to count the number of substrings in a binary string (`s`) that have an equal number of contiguous `0`s and `1`s. The provided solution uses a single pass to count contiguous groups of `0`s and `1`s while keeping track of the counts of these groups.

Here's a step-by-step breakdown of the approach:

- We maintain two counters: `count_zero` and `count_one` for the number of contiguous `0`s and `1`s respectively.
- We iterate through each character in the string:
  - If the character is `1`, we check if the previous character was also `1`. If yes, we increment `count_one`. If not, it indicates the end of a contiguous block of `0`s, so we add `min(count_zero, count_one)` to the result `res` (to count the valid substrings that can be formed up to that point). We then reset `count_one` to `1`.
  - If the character is `0`, we perform a similar operation but with `count_zero`.
- After iterating through the entire string, we account for the last set of contiguous characters by adding `min(count_zero, count_one)` to `res`.
- Finally, we return `res`, which contains the count of substrings.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the string `s`. We go through the string only once, which ensures a linear time complexity.
- **Space Complexity**: O(1). The space used is constant, as we use a fixed number of variables (`res`, `count_zero`, `count_one`, `prev_ch`) regardless of the input size.

## 3. Why This Approach is Efficient

This approach is efficient primarily due to its linear time complexity. By processing the string in a single pass (O(n)), we avoid the overhead associated with more naive approaches that may involve nested loops or multiple passes through the data.

Moreover, it effectively counts the substrings based on their groupings rather than generating all possible substrings, which would be computationally expensive (O(n^2) or worse). By maintaining counts of contiguous `0`s and `1`s, we can directly calculate how many valid substrings can be formed when transitioning between groups, thus efficiently summarizing the required counts without the need for additional data structures or excessive memory usage.

This strategy ensures that the solution is both time-efficient and space-efficient, making it well-suited for large input sizes typical in coding interview scenarios.

Runtime: undefined
Memory: 19740000
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # in o(n): conto gli 0 mentre vado avanti, o gli 1 e se matchano sommo
        res = 0
        count_zero = 0
        count_one = 0
        prev_ch = None
        for ch in s:
            if ch == '1':
                if prev_ch and prev_ch == '1':
                    count_one += 1
                else:
                    res += min(count_zero, count_one)
                    count_one = 1
            if ch == '0':
                if prev_ch and prev_ch == '0':
                    count_zero += 1
                else:
                    res += min(count_zero, count_one)
                    count_zero = 1

            prev_ch = ch

        #last steps:
        res += min(count_zero, count_one)
        return res


        

