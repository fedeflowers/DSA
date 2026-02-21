"""
```markdown
# Explanation of LeetCode Solution for "Prime Number of Set Bits in Binary Representation"

## 1. Brief Explanation of the Approach
The solution consists of three main methods:

- `_count_bits(el: int)`: This helper method counts the number of `1` bits (set bits) in the binary representation of a given integer `el`. It does this using a while loop that checks the least significant bit using the bitwise AND operation (`el & 1`), increments the count if the bit is set, and then right shifts `el` by one until all bits have been processed.

- `_is_prime(el: int)`: This method checks if a number `el` is a prime number. It first handles the special case where the number is `1`, returning `False` because `1` is not prime. For other numbers, it checks for divisibility from `2` up to the square root of `el`, returning `False` if a divisor is found and `True` otherwise.

- `countPrimeSetBits(left: int, right: int)`: This is the main function that iterates through all integers from `left` to `right` (inclusive). For each integer, it counts the number of set bits using `_count_bits` and checks if that count is prime using `_is_prime`. If it is prime, it increments the `num_set_bits_primes` counter. Finally, it returns the total count of integers in the specified range that have a prime number of set bits.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of the entire solution can be analyzed as follows:
  - The loop iterates through all integers between `left` and `right`, which means `O(n)` where `n = right - left + 1`.
  - For each number, `_count_bits` runs in `O(b)` where `b` is the number of bits in the integer (up to 32 for typical integer sizes), and `_is_prime` runs in `O(sqrt(m))` where `m` is the count of set bits (the max set bits is around `log_2(max_value)`).
  - Therefore, the overall time complexity can be approximated as:  
    **O(n * (b + sqrt(m)))**. Since `b` is a constant (at most 32), we can simplify it to:  
    **O(n * sqrt(m))**.

- **Space Complexity**: The space used by this solution is minimal:
  - It uses a constant amount of space for variables in the methods, so the space complexity is **O(1)**.

## 3. Why This Approach is Efficient
This approach is efficient mainly due to the following reasons:
- The use of bit manipulation for counting set bits (`_count_bits`) is fast and straightforward.
- Checking for primality up to the square root of the number is an effective method that avoids unnecessary computations for larger numbers.
- The solution loops from `left` to `right` once, ensuring we only traverse the range once, which is efficient for the problem at hand.
- Overall, the combination of bit manipulation and primality checking gives a reasonably efficient solution even for larger ranges of numbers.
```


Runtime: undefined
Memory: 19188000
"""

class Solution:
    def _count_bits(self, el: int):
        num_bits = 0
        while el:
            num_bits += el & 1
            el = el >> 1
        return num_bits

    def _is_prime(self, el: int):
        if el == 1:
            return False
        for i in range(2, int(math.sqrt(el))+1):
            if el % i == 0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        num_set_bits_primes = 0
        for i in range(left, right+1):
            if self._is_prime(self._count_bits(i)) == True:
                num_set_bits_primes += 1

        return num_set_bits_primes
