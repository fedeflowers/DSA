"""
```markdown
## Explanation of Solution

### 1. Brief Explanation of the Approach

The problem involves reducing an integer `n` to zero through a minimum number of operations where at each step, you can either subtract 1 or add a power of 2. The solution iteratively handles the bits of the number `n` from least significant to most significant.

- The algorithm uses a while loop that continues until `n` becomes zero.
- Inside the loop, it checks the last two bits of `n` to determine the optimal operation:
  - If the last two bits are `11`, it indicates that the number can be efficiently handled by adding the lowest set bit instead of subtracting multiple times. This is because adding can turn the two set bits into zeros, potentially carrying over to the next higher bit position.
  - If the last two bits are not `11`, the algorithm checks if the least significant bit (LSB) is a `1`. If it is, that means there's a need to subtract `1` to reset this bit.
- After processing the operations, `n` is right-shifted to move to the next bit.
  
Overall, the operations lead to counting how many times we need to perform either operation to reduce `n` to `0`.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(log n)
  - The loop runs until all bits of `n` have been processed, which takes logarithmic time relative to the value of `n` since the number of bits in `n` is proportional to `log n`.

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of space for storing variables (`res` and `n`), irrespective of the input size.

### 3. Why This Approach is Efficient

This approach is efficient because:
- By specifically handling patterns of bits (`11` and single `1`), it minimizes the number of operations needed to reduce `n`.
- The use of bitwise operations allows for constant-time checks and updates, which is faster than naive subtraction.
- It leverages the properties of binary numbers, making it suitable for operations that involve powers of 2, ensuring that the solution scales well with increasing values of `n`.
- The algorithm optimally chooses when to add instead of subtracting, which can lead to fewer overall steps, thereby achieving the goal of minimizing operations effectively.
```

Runtime: undefined
Memory: 19124000
"""

class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        # If there is only one '1': Subtract it (1 operation).

        # If there are two or more '1's: Add a power of 2 at the position of the first '1'. 
        # This turns the cluster into zeros and carries a '1' to the next bit (1 operation).
        while n > 0:
            # If the last two bits are '11', adding is better
            if (n & 3) == 3:
                n += (n & -n) # Add the lowest set bit
                res += 1
            else:
                # If it's a single '1', subtract it
                res += (n & 1)
                n >>= 1
        return res
