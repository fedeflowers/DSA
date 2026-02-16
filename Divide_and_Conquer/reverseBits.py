"""
```markdown
### Explanation of the LeetCode Solution for "Reverse Bits"

#### 1. Brief Explanation of the Approach
The given solution aims to reverse the bits of a 32-bit unsigned integer `n`. It does so by using a loop that iterates over each bit position from 0 to 31. During each iteration, the algorithm:
- Extracts the bit at the current position `i` of the integer `n` using the expression `(n >> i) & 1`. Here, `n >> i` shifts the bits of `n` to the right by `i` positions, and `& 1` isolates the least significant bit.
- Calculates the corresponding position in the reversed bit representation using the variable `reverse`, which starts at 31 (the last bit of the 32-bit integer) and decrements with each iteration.
- Adds the extracted bit, shifted to its reversed position, to the result `res` using the expression `((n >> i) & 1) << reverse`.

At the end of the loop, `res` contains the reversed bits, which is then returned.

#### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(1)
  - The algorithm has a fixed number of operations that depend only on the number of bits (32 for a 32-bit integer). Hence, it runs in constant time.
  
- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of space for variables (`res`, `reverse`, and `i`), irrespective of the input size.

#### 3. Why This Approach is Efficient
This approach is efficient mainly due to:
- **Direct Bit Manipulation**: The use of bitwise operations allows for efficient examination and modification of individual bits without the overhead of converting the integer into another format (like binary strings).
- **Fixed Size**: Since the size of the input is fixed at 32 bits, the number of iterations is constrained, leading to consistent performance regardless of the input value.
- **Minimal Memory Usage**: The algorithm does not utilize any additional data structures that would scale with input size, which means it remains memory efficient.

Overall, the solution effectively utilizes bitwise operations to achieve the desired result with a minimal time and space footprint.
```

Runtime: undefined
Memory: 19240000
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        reverse = 31
        for i in range(32):

            res += ((n>>i)&1) << reverse
            reverse -=1
            

        return res
        
