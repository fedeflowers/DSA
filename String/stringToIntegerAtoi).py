"""
```markdown
# Explanation of the LeetCode Solution for "String to Integer (atoi)"

## 1. Brief Explanation of the Approach
The solution implements a function `myAtoi` which converts a string representation of an integer into its actual integer format, following the rules of the `atoi` function common in programming languages. The approach includes the following key steps:

- **Trimming Whitespace:** The function first removes leading whitespace characters from the input string to avoid parsing issues.
- **Detecting Sign:** The function checks if the first non-whitespace character is either a '-' or '+' sign to determine if the resulting integer should be negative. It also manages the starting index for conversion.
- **Skipping Leading Zeros:** After detecting the sign, it skips any leading zeros to properly format the number.
- **Reading the Number:** The function iterates through the remaining characters in the string, appending digits to the resulting number while converting each character to an integer. The result is built by multiplying the current total by 10 (to shift it left) and adding the new digit.
- **Handling Overflow:** Before returning the result, the function checks if the computed integer exceeds the bounds of a 32-bit signed integer and adjusts it accordingly.

## 2. Time and Space Complexity Analysis
- **Time Complexity:** O(N), where N is the length of the input string. In the worst case, we iterate through the string twice: once for leading spaces/zeros and once for reading digits.
- **Space Complexity:** O(1). The solution uses a fixed amount of extra space for variables (like `res`, `start`, and `negative`), irrespective of the input size.

## 3. Why This Approach is Efficient
The approach is efficient due to its linear time complexity, which is optimal since every character in the input string might need to be inspected. The algorithm uses constant space, making it well-suited for scenarios where memory usage is a concern. The handling of potential overflow and various edge cases (like leading spaces and zeros) is also effectively managed in a straightforward manner, ensuring robustness against invalid inputs.
```

Runtime: undefined
Memory: 17596000
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        LOWER_BOUND = -2**31
        UPPER_BOUND = 2 **31 - 1
        # ignore leading whitespace
        s = s.lstrip()
        start = 0
        negative = False
        # signedness
        if s and s[0] == '-':
            negative = True
            start = 1
        elif s and s[0] == '+':
            start = 1
        # conversion
        #skip leading zeros:
        while s and start < len(s) and s[start] == '0':
            start += 1
        # read number
        while s and start < len(s) and s[start].isdigit():
            res = res*10 + int(s[start])
            start += 1
            
        if negative:
            res = -res
        if res > UPPER_BOUND:
            return UPPER_BOUND
        elif res < LOWER_BOUND:
            return LOWER_BOUND

        return res

