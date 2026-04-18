"""
# Explanation of LeetCode Solution for "Mirror Distance of an Integer"

## 1. Brief Explanation of the Approach

The task is to find the mirror distance of an integer, which is defined as the absolute difference between the integer and its reverse. The solution follows these steps:

- First, the integer `n` is converted to a string to facilitate reversal.
- The characters of the string are reversed and then joined back together to form the reversed string representation of the integer.
- This reversed string is then converted back to an integer (`n_rev`).
- Finally, the absolute difference between the original integer `n` and its reversed version `n_rev` is calculated and returned.

This allows us to compute the mirror distance efficiently in a straightforward manner.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The most time-consuming operations in this solution are converting the integer to a string and reversing the string. The time complexity for these operations is O(d), where `d` is the number of digits in the integer `n`. Thus, the overall time complexity is O(d).
  
- **Space Complexity**:
  - The space complexity is O(d) as well, due to the creation of the string representation of the integer and the reversed string. This space is needed to hold the intermediate string during the reversal process.

## 3. Why This Approach is Efficient

This approach is efficient for the following reasons:

- **Simplicity**: The method uses built-in Python string operations that are highly optimized. Using these functions takes advantage of Python's efficient handling of strings and sequences.
- **Concise**: The solution is implemented in very few lines of code, making it easy to understand and maintain. The concise nature of the implementation reduces the likelihood of bugs.
- **Directly Addresses the Problem**: The approach directly computes the required output without unnecessary computations, leveraging string manipulation to achieve the desired result quickly.

Overall, the solution is both efficient and easy to understand, making it suitable for tackling the problem at hand.

Runtime: undefined
Memory: 19160000
"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_rev = int("".join(list(str(n))[::-1]))
        return abs(n-n_rev)

