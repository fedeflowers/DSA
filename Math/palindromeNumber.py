"""
```markdown
## Explanation of the Solution for "Palindrome Number"

### 1. Brief Explanation of the Approach
The provided solution checks if a given integer `x` is a palindrome. A palindrome is a number that reads the same forward and backward. 

1. **Negative Check**: The function first checks if the number `x` is negative. If it is, it immediately returns `False` because negative numbers cannot be palindromes (due to the negative sign).
2. **Extracting Digits**: The function then enters a loop where it repeatedly extracts the last digit of `x` using `x % 10`, appending each digit to a list `l`. It then removes the last digit from `x` by performing integer division `x //= 10`.
3. **Palindrome Check**: After all digits have been collected in the list, the function checks if the list `l` is equal to its reverse (`l[::-1]`). If they are equal, `x` is a palindrome, and it returns `True`. Otherwise, it returns `False`.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the number of digits in the number `x`. This is because we have to loop through each digit of `x` and our final comparison of the list against its reverse also takes linear time relative to the number of items (digits).
  
- **Space Complexity**: O(n), for storing the digits of `x` in the list `l`. In the worst case, if `x` has `n` digits, the list will also contain `n` elements.

### 3. Why This Approach is Efficient
This approach is efficient because it clearly separates the concerns of extracting digits from the input number and evaluating the palindrome condition. 

- **Clarity**: The code is easy to understand and logically structured. It explicitly handles negative cases upfront and extracts digits in a straightforward manner.
- **Direct Comparison**: By using a list to store the digits, the palindrome check can be done in a single operation. While this does use extra space, it is manageable given the constraints of the problem.
- **Modular Process**: Each step is a simple operation (modulo and integer division), which are both O(1) operations, ensuring that even as `x` becomes larger, this method will still perform efficiently relative to the length of `x`.

In conclusion, this solution balances clarity and functionality effectively while maintaining linear time and space complexity which is acceptable for this problem context.
```

Runtime: undefined
Memory: 17864000
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        l = []
        while x > 0 :
            digit = x % 10
            x = x // 10
            l.append(digit)

        return l == l[::-1]
        
