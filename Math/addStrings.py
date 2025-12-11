"""
# Explanation of LeetCode Solution for "Add Strings"

## 1. Approach Explanation

The solution implements a straightforward algorithm to simulate the addition of two numbers represented as strings (`num1` and `num2`). The approach is akin to manual addition where digits are added starting from the least significant digit (the rightmost side) and moving to the most significant digit (the leftmost side), while carefully managing the carry from each digit addition. Here's a breakdown of the key steps:

- Convert the input strings into lists (`l1` and `l2`) for easier manipulation.
- Initialize a variable `carry` to 0, which will hold any value carried over from a digit to the next during the addition process.
- Prepare an empty list `res` to store resulting digits after addition.
- Use a loop that continues until there are no more digits to process in either string and no carry left:
  - Pop a digit from `l1` or set it to 0 if `l1` is exhausted.
  - Similarly, pop a digit from `l2` or set it to 0 if `l2` is exhausted.
  - Convert the popped characters to integers, compute the sum of the digits along with any carry, and then determine the new carry and the current digit to append to the result.
- Finally, since the digits were added in reverse order (from least significant to most significant), reverse the `res` list and join its elements to form the final result string. 

## 2. Time and Space Complexity Analysis

### Time Complexity
- The time complexity is O(max(N, M)), where N and M are the lengths of `num1` and `num2`, respectively. This is because the algorithm essentially processes each digit of the strings once. The maximum length ensures that all digits from both strings are accounted for, including any carry.

### Space Complexity
- The space complexity is O(max(N, M)) as well, primarily due to the storage of the result list `res`, which can grow to the length of the larger input string if all digits must be kept.

## 3. Efficiency of This Approach

This approach is efficient for several reasons:

- **Simplicity and Clarity**: The simulation of manual addition makes the code easy to understand. The use of lists and pops allows straightforward manipulation of the digits.
- **Handles Varying Lengths**: The algorithm can handle strings of different lengths naturally due to the checks for exhausted lists and the carry.
- **No Additional Libraries**: The solution does not rely on converting the entire string to an integer (which could lead to overflow issues for very large numbers), making it robust against large inputs.
- **In-Place Processing**: Popping elements from the end of lists and appending to `res` minimizes the need for creating additional copies of data. 

Overall, the algorithm is efficient and effectively handles the addition of two potentially very large numbers represented as strings.


Runtime: undefined
Memory: 18516000
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
                d1 = 0
            if l2:
                d2 = l2.pop()
            else:
                d2 = 0
            curr_digit = int(d1) + int(d2) + carry
            carry = curr_digit // 10
            res.append(str(curr_digit % 10))

        return "".join(res[::-1])
