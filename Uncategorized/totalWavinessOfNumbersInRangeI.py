"""
```markdown
## Explanation of the LeetCode Solution for "Total Waviness of Numbers in Range I"

### 1. Brief Explanation of the Approach

The provided solution calculates the "waviness" of all numbers in a given range [num1, num2] by employing a nested function called `waviness(num)`. The task revolves around identifying local maxima and minima—defined as:

- **Local Maximum**: A digit that is greater than its neighboring digits.
- **Local Minimum**: A digit that is less than its neighboring digits.

The `waviness` function computes the number of such local extremes in a given number. It does this by iterating through each digit of the number from the least significant to the most significant, comparing each digit with its previous and next neighbor. If it finds a local maximum or minimum, it increments the `res` variable that counts the total waviness for that number.

After defining `waviness`, the solution iterates through the specified range from `num1` to `num2`, invoking the `waviness` function for each number and summing the results to compute the overall waviness for the range.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity is O(K * M), where:
  - K = number of integers in the range [num1, num2], which is equal to (num2 - num1 + 1).
  - M = the maximum number of digits in the largest number in the range (in the worst case, this is O(log10(num2))).
  
  Thus, the overall time to compute the waviness for all numbers in the range is proportional to the number of integers multiplied by the number of digits processed for each integer.

- **Space Complexity**: The space complexity is O(1) in terms of additional space used. The algorithm uses a fixed number of variables regardless of input size, thus requiring constant extra space.

### 3. Why This Approach is Efficient

This approach is efficient due to its linear traversal through each number's digits, allowing the function to derive the waviness in a straightforward manner without the need for auxiliary data structures (e.g., lists or arrays). The calculation of waviness directly accumulates counts in simple conditional statements, making it computationally inexpensive per number.

Furthermore, the nested function neatly encapsulates the logic of calculating waviness, promoting modular design. By processing digits in their natural order and leveraging mathematical operations for the comparisons, the algorithm remains efficient and easy to understand.

The direct iteration over the specified numeric range and efficient processing of individual digits makes this solution practical for typical input sizes encountered in competitive programming.
```

Runtime: undefined
Memory: 17872000
"""

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res = 0
        def waviness(num):
            res = 0
            prev = None
            l = len(str(num))
            while num != 0:
                curr = num % 10
                num //= 10
                next = num%10
                if num == 0:
                    break
                if prev is not None:
                    if prev < curr  and curr > next :
                        res += 1
                    elif prev > curr and curr < next:
                        res += 1

                prev = curr
            return res

        for i in range(num1, num2+1):
            res += waviness(i)
        
        return res
