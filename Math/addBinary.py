"""
```markdown
# Explanation of the LeetCode Solution for "Add Binary"

## 1. Brief Explanation of the Approach
The given solution implements a method to add two binary strings (representations). The primary steps taken in the approach are:

- **Reverse the Input Strings**: The binary strings are reversed to facilitate the addition from the least significant bit (rightmost side) to the most significant bit (leftmost side). This mimics how addition is performed manually.
  
- **Loop Through Each Bit**: The solution uses a loop that continues until all bits from both strings are processed (even if one string is longer than the other) or there is a carry that needs to be added. During each iteration:
  - It extracts the current bit from each string, converting it to an integer. If the index exceeds the length of the string, it defaults to 0.
  - It calculates the sum of the bits from both strings and the carry from the previous addition.
  - It determines the current carry for the next iteration and stores the result (either 0 or 1) for the current bit in a results list.

- **Reverse the Result**: Finally, since the result was constructed in reverse order, the method reverses the results list before joining it into a final binary string output.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(max(N, M)), where N is the length of string `a` and M is the length of string `b`. The loop iterates through each bit of the longer string (including cases with carries). 

- **Space Complexity**: O(max(N, M)), as we create a list `res` that has at most the length equal to the longer of the two binary strings.

## 3. Why This Approach is Efficient
This approach is efficient because:
- It processes each bit in constant time, ensuring that the overall time complexity remains linear with respect to the size of the input strings.
- The space complexity is kept to a minimum, only requiring space for the result that is directly proportional to the length of the longer input string.
- The use of basic arithmetic and conditionals within the loop ensures minimal overhead, making the method straightforward and easy to understand. The approach efficiently handles cases where the input strings have different lengths and manages carry succinctly.
```

Runtime: undefined
Memory: 19480000
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = []
        i=0
        while i < max(len(a), len(b)) or carry:
            curr_a = int(a[i]) if i < len(a) else 0
            curr_b = int(b[i]) if i < len(b) else 0

            res.append(str((curr_a + curr_b + carry) %2))
            carry = 1 if curr_a + curr_b + carry > 1 else 0
            i+=1

        return "".join(res[::-1])
