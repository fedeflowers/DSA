"""
```markdown
# Explanation of the LeetCode Solution for "Binary Number with Alternating Bits"

## 1. A Brief Explanation of the Approach
The solution provided determines whether a binary number has alternating bits (i.e., the bits alternate between 0 and 1) by using a combination of bit manipulation techniques. 

### Steps:
1. **XOR Operation**: The expression `n ^ (n >> 1)` computes the XOR of `n` with its right-shifted version. If `n` has alternating bits, the XOR result will produce a binary number consisting entirely of 1s. This is because each bit in `n` differs from the bit next to it in the right-shifted version.
   - For example, if `n = 10` (binary `1010`), `n >> 1` will yield `5` (binary `0101`), and `10 ^ 5` results in `15` (binary `1111`).

2. **Checking for Power of Two**: After obtaining the value from the XOR operation, we add 1 to this result. For a number that consists of all 1s (like `111...111`), adding 1 will yield a power of two (such as `1000...000`). A property of powers of two is that they have only a single bit set to 1 when expressed in binary.

3. **Final Check**: The final step checks whether `(x & (x + 1)) == 0`, where \( x \) is the result of the XOR operation. If this condition holds true, it indicates that \( x \) was a solid block of 1s, confirming that the original number `n` indeed had alternating bits.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of this approach is \( O(1) \). It performs a constant number of operations regardless of the size of the input number `n`.
- **Space Complexity**: The space complexity is also \( O(1) \) since the solution uses only a fixed amount of space for variable storage and does not depend on the size of `n`.

## 3. Why This Approach is Efficient
The efficiency of this approach lies in the simplicity of bit manipulation. Using XOR and bitwise operations allows for quick validation of the alternating bit condition without the need for complex iterations or additional data structures. This leads to minimal processing time and constant space usage, making it ideal for problems involving binary representations. The method leverages mathematical properties of binary numbers, leading to a concise and effective solution.
```

Runtime: undefined
Memory: 19384000
"""

# class Solution:
#     def hasAlternatingBits(self, n: int) -> bool:
#         while n > 0:
#             last_bit = n & 1
#             n = n >> 1
#             if n & 1 == last_bit:
#                 return False

#         return True
        # 1. XOR ($n \oplus (n \gg 1)$)If bits alternate ($10101...$), then $(n \gg 1)$ shifts everything by one position ($01010...$).Performing XOR compares each bit with its neighbor.Because every bit is different from its neighbor, XOR results in a sequence of all 1s.Example: If $n = 1010_2 (10)$, then $n \oplus (n \gg 1)$ is $1010 \oplus 0101 = 1111_2$.2. The Power-of-Two CheckLet $x = n \oplus (n \gg 1)$. If $n$ was alternating, $x$ is now a binary number like $111...1$.Adding 1 to $x$ ($111 + 1$) results in a power of two ($1000$).A property of any power of two ($y$) is that $y \ \& \ (y-1) == 0$.In this formula, $y = x + 1$ and $y - 1 = x$.Therefore, $(x \ \& \ (x + 1)) == 0$ returns True only if $x$ was a solid block of 1s.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return ((n ^ (n >> 1)) & ((n ^ (n >> 1)) + 1)) == 0
