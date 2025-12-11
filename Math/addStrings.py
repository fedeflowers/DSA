"""
## Explanation of the LeetCode Solution for "Add Strings"

### 1. Brief Explanation of the Approach

The problem "Add Strings" requires adding two non-negative integers represented as strings without converting them to integers directly. The provided solution utilizes a two-pointer technique where digits are processed from the least significant to the most significant (right to left).

Here's a breakdown of the approach:

- **Initialization**: Two lists are created from the input strings `num1` and `num2` to facilitate popping digits one at a time. A `carry` variable is initialized to zero to keep track of any value that needs to be carried over to the next significant digit.

- **Loop through Digits**: A while loop continues until both lists are empty and there is no carry left:
  - If there are digits remaining in `l1` (from `num1`), the last digit is popped; otherwise, a default value of "0" is assigned.
  - The same logic applies to `l2` (from `num2`).
  - The current digit sum is calculated by converting these characters to their respective integer values using ASCII operations: `ord(d1) - ord('0')` converts the character to its integer representation.

- **Carry Management**: After calculating the current digit sum, the carry for the next iteration is updated, and the least significant digit (obtained using `% 10`) is added to the result list.

- **Result Compilation**: After the loop, the result list is reversed to represent the final answer correctly, and the digits are concatenated into a single string.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: \( O(N + M) \)
  - Where \( N \) is the length of `num1` and \( M \) is the length of `num2`. This is because the algorithm goes through each digit of both input strings once.

- **Space Complexity**: \( O(N + M) \)
  - The space is primarily used for storing the result in a list that can potentially hold all digits of the sum of the two numbers (since they could be of similar size), and also for the lists holding the digits of `num1` and `num2`.

### 3. Why This Approach is Efficient

This approach is efficient due to several reasons:

- **No Type Conversion Overhead**: By avoiding conversion of the entire string into an integer, the code maintains the integrity of very large numbers that might exceed standard integer limits. Instead, it works directly with the string representations.

- **Direct Character Manipulation**: Using ASCII values for digit conversion is a direct way to handle character-to-integer conversions without added complexity.

- **Single Pass Addition**: The method processes both strings in a single pass and handles digit carry naturally, which is in line with how addition is performed manually, making it simpler and more intuitive.

This combination of techniques allows the solution to handle input strings of arbitrary lengths efficiently and correctly.

Runtime: undefined
Memory: 18604000
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = list(num1)
        l2 = list(num2)
        carry = 0
        res = []
        while l1 or l2 or carry:
            if l1:
                d1 = l1.pop()
            else:
                d1 = "0"
            if l2:
                d2 = l2.pop()
            else:
                d2 = "0"
            # curr_digit = int(d1) + int(d2) + carry # this can be
            curr_digit = ord(d1) - ord('0') + ord(d2) - ord('0') + carry
            carry = curr_digit // 10
            res.append(str(curr_digit % 10))

        return "".join(res[::-1])
