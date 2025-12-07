"""
```markdown
## Explanation of the Solution for "Count Odd Numbers in an Interval Range"

### 1. Approach Explanation
The given solution for counting the odd numbers in a range `[low, high]` utilizes a mathematical approach to determine how many odd numbers there are without explicitly iterating through the range. 

- The variable `diff` is calculated as `high - low + 1`, representing the total number of integers in the inclusive range from `low` to `high`.
- The code checks if `low` is even or odd:
  - If `low` is even, the odd numbers from `low` to `high` will occur at every alternate position starting from `low + 1`. Thus, the total count of odd numbers can be computed as `diff // 2`.
  - If `low` is odd, the counting starts from `low` itself, which is odd. Therefore, the formula will count one more odd number, calculated as `math.ceil(diff / 2)`.

This logic effectively divides the total count of numbers by 2, accounting for the parity of the starting number.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(1)
  - The solution performs a constant number of operations regardless of the input size. It computes a few arithmetic expressions and conditions.
  
- **Space Complexity**: O(1)
  - The solution uses a fixed amount of space for the variables `diff` and does not utilize any additional data structures or lists that grow with input size.

### 3. Efficiency of the Approach
This approach is efficient because it eliminates the need for iteration over the range of numbers, which would be less optimal especially for large values of `low` and `high`. Instead, it relies on simple arithmetic operations which are computed in constant time, making it very quick. This efficiency is particularly useful in scenarios where the interval size can be large (for example, if `low` and `high` are both in the order of 10^9). The solution is optimal and handles all edge cases smoothly with basic checks for even and odd starting points.
```


Runtime: undefined
Memory: 17820000
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low + 1
        if low % 2 == 0: #start with even
            return diff // 2
        else: #starts with odd
            return math.ceil(diff/2)
            

