"""
Sure! Here’s a detailed explanation of the LeetCode solution for the problem "Binary Prefix Divisible By 5".

## Explanation of the Approach

The problem asks us to determine if the decimal value of binary prefixes formed by the elements in the array `nums` is divisible by 5. The elements of `nums` are either 0 or 1, which represent binary digits.

### Key Steps:
1. **Initialization**: We create an empty list `final` to store the results and a variable `curr_res` to hold the current binary value as we iterate through the elements in `nums`.
  
2. **Binary Conversion**: For each element `el` in `nums`, we update `curr_res` using bit manipulation:
   - `curr_res = curr_res << 1` shifts the current value to the left by one bit (i.e., multiplying by 2).
   - The operation `| el` adds the current element (`0` or `1`) as the least significant bit.
   This effectively builds the binary number represented by the prefix.

3. **Divisibility Check**: After updating `curr_res`, we check if this number is divisible by 5 by evaluating `curr_res % 5 == 0`. We append the result (True/False) to the `final` list.

4. **Return**: Finally, we return the list `final`, which contains boolean values indicating whether each binary prefix is divisible by 5.

## Time and Space Complexity Analysis

### Time Complexity:
- The algorithm iterates through the input list `nums` once, where the length of `nums` is `n`. All operations inside the loop (shifting, bitwise OR, and modulus) are constant time operations.
  
Thus, the time complexity is O(n).

### Space Complexity:
- The `final` list will have the same length as `nums`, which requires O(n) space.
  
So, the space complexity is also O(n) for the output list.

## Why This Approach is Efficient

1. **Direct Handling of Binary Values**: The use of bitwise operations (`<<` and `|`) allows us to efficiently build the binary number without converting to decimal explicitly at each step. This keeps the operations fast—O(1) for each element processed.

2. **Single Pass through Input**: The algorithm processes each element of the input list just once, making it efficient in terms of time.

3. **Modular Arithmetic**: The check for divisibility by 5 is efficiently incorporated into the prefix build-up, leveraging the properties of modular arithmetic rather than forcing additional operations.

This combination of techniques yields an efficient solution to the problem, handling both computation and memory usage effectively. 

Overall, the solution elegantly builds up the binary prefixes and checks for divisibility in a streamlined manner.

Runtime: N/A
Memory: N/A
"""

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        final = []
        curr_res = 0
        for el in nums:
            curr_res = curr_res <<1 | el
            final.append(curr_res % 5 == 0)
        return final
