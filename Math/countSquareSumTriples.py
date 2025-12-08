"""
## Explanation of the LeetCode Solution for "Count Square Sum Triples"

### 1. Approach

The goal of the problem "Count Square Sum Triples" is to count the number of distinct triples (a, b, c) such that \(a^2 + b^2 = c^2\) with the constraints \(1 \leq a, b, c \leq n\). 

The approach taken in the provided solution involves iterating over all pairs of integers (a, b) with the inner loop starting from \(a + 1\) to ensure that pairs are distinct and that \(a < b\). For each pair \(a\) and \(b\), it calculates \(c\) as the integer square root of \(a^2 + b^2\), after adding 1 to ensure it rounds correctly when checking if \(c\) is an integer. The condition checks if \(c\) is less than or equal to \(n\) and whether \(c^2\) equals \(a^2 + b^2\). If both conditions are satisfied, it increments the result by 2, accounting for the pairs (a, b) and (b, a) as valid combinations.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The solution involves two nested loops where `a` ranges from 1 to `n` and `b` ranges from `a + 1` to `n`. The maximum iterations for `b` given a fixed `a` can be approximated as \(n\). Thus, the total complexity can be expressed as follows:
  \[
  O(n^2)
  \]
This comes from the nested iteration structure, as for every `a`, we iterate through `b`.

- **Space Complexity**: The space complexity is \(O(1)\) because aside from the input and output, we are only using a few variable counters and no extra data structures that grow with `n`.

### 3. Why This Approach is Efficient

This approach is efficient for several reasons:
- **Direct Calculation**: By directly calculating \(c\) from \(a\) and \(b\), we avoid nested iterations for `c`, thus minimizing unnecessary computations.
- **Distinct Pairs**: The solution naturally ensures that pairs (a, b) are distinct by ranging `b` starting from `a + 1`, which eliminates duplicate counting without needing additional checks.
- **No Duplication**: Since it counts each valid (a, b) configuration twice (for ordering purposes) at once, it elegantly handles the symmetry in the problem.
- **Limit Check**: Checking \(c \leq n\) before confirming \(c^2 = a^2 + b^2\) prevents unnecessary operations and ensures that the solution adheres to the bounds given in the problem statement.
  
Overall, the method is straightforward and efficient within reasonable constraints for `n`, making it a robust solution to the problem.

Runtime: undefined
Memory: 17912000
"""

# class Solution:
#     def countTriples(self, n: int) -> int:
#         #brute force O(n**2)
#         squares = []
#         res = 0
#         for i in range(1, n + 1):
#             squares.append(i**2)

#         fast_sq = set(squares)

#         for i in range(len(squares)):
#             for j in range(i+1, len(squares)):
#                 if squares[i] + squares[j] in fast_sq:
#                     res += 2

#         return res

from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        # enumerate a and b
        for a in range(1, n + 1):
            for b in range(a+1, n + 1):
                # determine if it meets the requirements
                c = int(sqrt(a**2 + b**2 + 1))
                if c <= n and c**2 == a**2 + b**2:
                    res += 2
        return res
