"""
# Explanation of the LeetCode Solution for "Multiply Strings"

## 1. Approach Explanation
The solution to the "Multiply Strings" problem involves simulating the multiplication of two numbers represented as strings without converting them to integers directly. Here's a breakdown of the approach:

- **Initial Check**: The algorithm first checks if either of the input strings `num1` or `num2` is "0". If so, it directly returns "0" since any number multiplied by zero results in zero.

- **Array for Results**: A result array `res` of length `n` (where `n` is the combined length of both input strings) is initialized with zeros. This array will hold the intermediate results of the multiplication.

- **Nested Loops for Digit Multiplication**: The algorithm iterates over the digits of `num1` and `num2` in reverse order. This way, the least significant digits are processed first. For each pair of digits `d1` (from `num1`) and `d2` (from `num2`), the product `int(d1) * int(d2)` is computed and added to the corresponding index in the result array. The index is determined by the sum of the positions of the digits being multiplied (`i + j`).

- **Carry Propagation**: After computing all products, a single pass is carried out to handle carries. Each index `k` in the result array is processed to ensure that it holds a single digit; if any index has a value greater than 9, it adds the carry to the next index.

- **Removing Leading Zeros**: If the most significant index of the `res` array (the last index) is zero after all carries are propagated, it indicates that the result is of lower length; hence, the last element is removed.

- **Final Output**: The final result is constructed by reversing the result array and concatenating the digits together to form the final product string.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this solution is O(m * n), where `m` is the length of `num1` and `n` is the length of `num2`. This is due to the nested loops that iterate through both strings to calculate the product of each digit combination.

- **Space Complexity**: The space complexity is O(m + n) because of the `res` array that stores the individual digit results. The length of this array is the sum of the lengths of the two input strings.

## 3. Efficiency of the Approach
This approach is efficient because:

- **Direct String Manipulation**: It avoids converting strings to integers, which can lead to overflow issues for large numbers. This is especially significant when dealing with strings that represent very large integers.

- **Carry Management**: The single pass for carrying values ensures that the result is correctly formed in a simple and effective manner.

- **Digit-by-Digit Multiplication**: This simulates the grade-school method of multiplication, which is both intuitive and straightforward for implementing string-based arithmetic.

Overall, this solution is both a practical and scalable way to handle string multiplications in Python while handling edge cases and large numbers effectively.

Runtime: undefined
Memory: 19276000
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n = len(num1) + len(num2)
        res = [0] * n

        # Iterate in reverse so index 0 = least significant digit
        for i, d1 in enumerate(reversed(num1)):
            for j, d2 in enumerate(reversed(num2)):
                res[i + j] += int(d1) * int(d2)

        # Single carry-propagation pass
        for k in range(n - 1):
            res[k + 1] += res[k] // 10
            res[k] %= 10

        # Strip leading zero (most significant end)
        if res[-1] == 0:
            res.pop()

        return "".join(str(x) for x in reversed(res))
