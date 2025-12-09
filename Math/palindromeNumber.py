"""
```markdown
## Explanation of the LeetCode Solution for "Palindrome Number"

### 1. Brief Explanation of the Approach
The solution to the Palindrome Number problem can be broken down into systematic checks and manipulations of the number `x`. 

- **Initial Checks**:
  - If `x` is negative, it can't be a palindrome since palindromes read the same forward and backward.
  - If `x` ends with a `0` and is not `0` itself, it can't be a palindrome (e.g., `10`, `20`, etc.), since the first digit (in the forward direction) would be non-zero while the last digit (in the reverse direction) would be zero.
  
- **Main Logic**:
  - The algorithm proceeds by reversing half of the number. This is achieved using a `while` loop that continues until `x` is greater than `revertedNumber`.
  - In each iteration of the loop, the last digit of `x` is retrieved using `% 10` and added to `revertedNumber`. 
  - Simultaneously, `x` is reduced by removing its last digit using integer division by `10`.
  
- **Final Comparison**:
  - Once the loop ends, there are two scenarios to check for a palindrome:
    - If the length of the palindrome is even, `x` should be equal to `revertedNumber`.
    - If the length is odd, the middle digit can be ignored. Thus, `x` should be equal to `revertedNumber // 10`.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The time complexity is **O(log10(n))**, where `n` is the value of `x`. This is because the algorithm essentially reduces the number of digits in `x` by half through integer division during the palindrome check.
  
- **Space Complexity**: 
  - The space complexity is **O(1)** since only a fixed amount of additional space is used (i.e., `revertedNumber`) regardless of the size of `x`. We are not utilizing any data structures that scale with input size.

### 3. Why this Approach is Efficient
This approach is efficient because:
- It avoids converting the integer `x` into a string or array, which would require additional space.
- By only reversing half of the number, it minimizes operations while still accurately determining if the number is a palindrome, hence optimizing the time complexity.
- The checks for negative numbers and trailing zeros significantly reduce unnecessary computations, allowing the algorithm to quickly rule out non-palindrome scenarios.

Overall, this solution effectively utilizes mathematical operations to arrive at a correct and efficient determination of whether a number is a palindrome.
```

Runtime: undefined
Memory: 17896000
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
        
#We divided the input by 10 for every iteration, so the time complexity is O(log10(n))
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
