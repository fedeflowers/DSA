"""
```markdown
## Explanation of the LeetCode Solution for "Palindrome Number"

### 1. Approach Explanation

The given solution checks if an integer \( x \) is a palindrome (i.e., it reads the same forwards and backwards). The approach involves the following key steps:

- **Initial Checks**: 
  - If \( x \) is negative, it cannot be a palindrome (return False).
  - If \( x \) ends with a `0` and is not `0` itself, it cannot be a palindrome (since a palindrome cannot start with zero). Thus, return False.

- **Reversing Half of the Number**: 
  - The algorithm then initializes a variable `revertedNumber` to store the reverse of the digits of \( x \).
  - By reversing only half of the digits, the algorithm avoids creating a complete reversed string, which can increase space usage. 
  - The while loop continues until `x` is less than or equal to `revertedNumber`. This way, we compare the digits progressively, essentially building the reversed number.

- **Final Comparison**: 
  - After the loop, there are two scenarios to check:
    - If \( x \) is equal to `revertedNumber`: this means we have found a palindrome.
    - If \( x \) is equal to `revertedNumber // 10`: this accounts for cases with an odd number of digits where the middle digit can be ignored (e.g., in 12321, after processing we might have \( x = 12 \) and `revertedNumber = 123`).

### 2. Time and Space Complexity Analysis

- **Time Complexity**: \( O(\log_{10} n) \)
  - The loop runs a number of times proportional to the number of digits in \( x \), which is \( \log_{10} n \).

- **Space Complexity**: \( O(1) \)
  - The solution only uses a few variables (`revertedNumber` and \( x \)), making use of integer operations without extra space for arrays or strings.

### 3. Efficiency of This Approach

This approach is efficient mainly due to its use of constant space and minimal comparisons. By only reversing half of the number, it reduces the amount of processing required while ensuring correctness. Additionally, special cases are handled before performing any significant calculations, thus avoiding unnecessary operations for known non-palindrome cases. The overall performance is optimal for this problem since it leverages mathematical properties of numbers and minimizes memory overhead.
```

Runtime: undefined
Memory: 17616000
"""

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         l = []
#         while x > 0 :
#             digit = x % 10
#             x = x // 10
#             l.append(digit)

#         return l == l[::-1]
        

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber//10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber or x == revertedNumber // 10
