"""
# Explanation of the LeetCode Solution for "Binary Number with Alternating Bits"

## 1. Brief Explanation of the Approach

The problem "Binary Number with Alternating Bits" requires us to determine if the binary representation of a given number \( n \) has alternating bits (i.e., no two consecutive bits are the same). The code provided defines a method `hasAlternatingBits` that takes an integer \( n \) as input and performs the following steps:

- It enters a loop that continues until \( n \) becomes zero.
- Inside the loop, it retrieves the last bit of \( n \) using the bitwise AND operation (`last_bit = n & 1`).
- It then shifts \( n \) one bit to the right (`n = n >> 1`), effectively removing the last bit.
- It checks the new last bit of \( n \) (`n & 1`) to see if it is the same as the previous last bit stored in `last_bit`.
- If the two bits are the same, the function returns `False`, as this indicates the bits are not alternating.
- If the loop completes without finding two consecutive bits that are the same, the function returns `True`, confirming that the bits alternate correctly.

## 2. Time and Space Complexity Analysis

- **Time Complexity:** \( O(k) \), where \( k \) is the number of bits in the binary representation of the number \( n \). In the worst case, this loop iterates through all bits of \( n \) to check for alternation.
  
- **Space Complexity:** \( O(1) \), since the function uses a fixed amount of space for the variables (`last_bit`) and does not rely on any data structures that grow with input size.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **Bitwise Operations:** The use of bitwise operations allows for constant time checks and manipulations of the individual bits without requiring any additional space (like arrays or strings to represent the binary form). This minimizes overhead and leads to efficient performance.
  
- **Early Exit:** The function can terminate early upon finding a pair of consecutive identical bits, thus potentially reducing the number of iterations in cases where the input number has many bits but does not alternate early on.

- **Minimal Resource Usage:** The space complexity remains constant, which is advantageous when dealing with large numbers. This approach does not depend on additional memory allocation proportional to the input size, which can be critical in environments with strict memory limits.

Overall, this code efficiently checks for alternating bits while ensuring optimal time and space usage.

Runtime: undefined
Memory: 19408000
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            last_bit = n & 1
            n = n >> 1
            if n & 1 == last_bit:
                return False

        return True
