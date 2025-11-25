"""
```markdown
## Explanation of the Solution for "Smallest Integer Divisible by K"

### 1. Approach Explanation
The problem "Smallest Integer Divisible by K" asks us to find the smallest positive integer consisting solely of the digit 1 that is divisible by a given integer K. The code provided defines a method `smallestRepunitDivByK` that implements the following logic:

- **Early Return for Divisibility:** 
  - If `k` is divisible by 2 or 5, the function returns -1 immediately, as a number consisting solely of 1s cannot be divisible by any even number or multiples of 5.

- **Iterative Remainder Calculation:**
  - The algorithm uses a loop to build numbers that consist solely of the digit 1. Instead of constructing the integer itself (which can grow large), we compute the remainder of `111...1` when divided by K.
  - In each iteration:
    - The length of the current number (in terms of digits) is increased.
    - We compute the new remainder by updating it according to the formula: `remainder = (remainder * 10 + 1) % k`. This represents appending a new '1' to the end of the number.
    
- **Check for Divisibility:**
  - If at any point, the remainder becomes 0, the function returns the current `length`, since it indicates that the number formed by 'length' ones is divisible by K.
  
- **Cycle Detection with Seen Remainders:**
  - To avoid looping indefinitely (for example if no such number exists), the algorithm keeps track of already-seen remainders using a set. If a remainder is encountered that has been seen before without finding a solution, the function returns -1, indicating that there's no such number.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** O(K)
  - In the worst case, the algorithm may take up to K iterations before either finding a valid length or determining that no valid "1" number can be formed. Since each iteration involves simple arithmetic operations, the overall time complexity is bounded by O(K).

- **Space Complexity:** O(K)
  - The space complexity is also O(K) due to the storage of encountered remainders in a set. In the worst case, if all remainders from 1 to K-1 are stored, the space used will be proportional to K.

### 3. Efficiency of the Approach
This approach is efficient for the following reasons:
- **Avoids Large Number Computation:** 
  - Instead of constructing potentially massive integers consisting of '1's, it works with remainders, which are manageable and compact.
  
- **Cycle Detection:** 
  - By storing seen remainders, the algorithm efficiently detects if it's falling into a cycle without finding a solution, thereby preventing endless loops.

- **Early Stopping Conditions:** 
  - By checking a few divisibility conditions upfront, the algorithm can quickly reject impossible cases, leading to faster termination in cases where K is an even number or a multiple of 5.

Overall, the combination of working directly with mathematical properties (remainders) and utilizing efficient data structures (sets) makes this algorithm both effective and efficient for the problem at hand.
```

Runtime: undefined
Memory: 21608000
"""

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k% 2 == 0 or k % 5 == 0:
            return - 1

        remainder = 0
        length = 0

        seen_remainders = set()

        while True:
            length += 1
            remainder = (remainder * 10 + 1) % k

            if remainder == 0:
                return length

            if remainder in seen_remainders:
                return - 1

            seen_remainders.add(remainder)
