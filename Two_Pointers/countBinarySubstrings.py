"""
## Explanation of the Solution for "Count Binary Substrings"

### 1. A Brief Explanation of the Approach
The problem "Count Binary Substrings" requires counting the number of substrings that contain equal numbers of '0's and '1's. The approach employed in the provided code utilizes a two-pointer technique that iterates through the string while keeping track of the lengths of contiguous segments of '0's and '1's.

Here's a step-by-step breakdown of the logic:
- **Initialization:** We start with three variables:
  - `ans`: to store the total count of valid binary substrings.
  - `prev`: to keep track of the length of the previous segment of characters.
  - `cur`: to keep track of the length of the current segment of characters.

- **Iteration:** We iterate through the string starting from the second character (index 1):
  - If the current character (`s[i]`) is different from the previous character (`s[i-1]`), it indicates a change in the segment:
    - We add the minimum of `prev` and `cur` to `ans`. This works because you can form substrings from the two segments that end at this point.
    - Update `prev` to the value of `cur` (previous segment's length) and reset `cur` to 1 for the new segment.
  - If the characters are the same, we just increase the `cur` counter.

- **Final Addition:** After the loop completes, we need to account for any remaining segments by adding `min(prev, cur)` once more to `ans`.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** O(n), where n is the length of the input string `s`. The algorithm processes each character exactly once.
  
- **Space Complexity:** O(1). The algorithm uses a constant amount of space for the `ans`, `prev`, and `cur` variables, regardless of the size of the input.

### 3. Why This Approach is Efficient
This approach is efficient due to its linear time complexity combined with constant space usage. The key points that contribute to the efficiency are:
- **Single Pass Iteration:** The entire string is processed in a single iteration, meaning that we derive counts without the need for nested loops, which could lead to higher time complexity.
  
- **Optimal Counting with Minimums:** By leveraging the minimum of the previous and current segments, the solution efficiently counts valid substrings without the need to explicitly create or store each substring. This allows for optimal counting of valid pairs directly during the traversal.

In conclusion, the solution intelligently consolidates the required counts while maintaining clarity and efficiency, making it an optimal solution for the problem at hand.

Runtime: undefined
Memory: 19624000
"""

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         # in o(n): conto gli 0 mentre vado avanti, o gli 1 e se matchano sommo
#         res = 0
#         count_zero = 0
#         count_one = 0
#         prev_ch = None
#         for ch in s:
#             if ch == '1':
#                 if prev_ch and prev_ch == '1':
#                     count_one += 1
#                 else:
#                     res += min(count_zero, count_one)
#                     count_one = 1
#             if ch == '0':
#                 if prev_ch and prev_ch == '0':
#                     count_zero += 1
#                 else:
#                     res += min(count_zero, count_one)
#                     count_zero = 1

#             prev_ch = ch

#         #last steps:
#         res += min(count_zero, count_one)
#         return res

class Solution:
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)

        

