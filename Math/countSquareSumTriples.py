"""
```markdown
### Explanation of the Solution for "Count Square Sum Triples"

1. **Approach:**
   The solution uses a nested loop to iterate over pairs of integers \(a\) and \(b\) from 1 to \(n\). For each pair, it calculates the potential integer \(c\) such that the equation \(a^2 + b^2 = c^2\) holds true. The integer \(c\) is computed as the integer square root (with an adjustment of +1) of the sum \(a^2 + b^2\). If \(c\) is within the bounds (i.e., \(c \leq n\)) and the equation \(c^2 = a^2 + b^2\) is valid, it increments the result counter `res`. The output will be the total count of valid triples \((a, b, c)\).

2. **Time and Space Complexity Analysis:**
   - **Time Complexity:** The solution has a time complexity of \(O(n^2)\) due to the nested loops iterating through possible values of \(a\) and \(b\), both of which can range up to \(n\). Thus, the total operations performed will be roughly proportional to \(n^2\).
   - **Space Complexity:** The space complexity is \(O(1)\), as we are using only a fixed amount of space for the integer variables (`res`, `a`, `b`, `c`) and not utilizing any additional data structures that grow with the input size.

3. **Efficiency of the Approach:**
   This method is efficient for the problem because:
   - It only checks valid pairs of integers instead of generating all possible triples. By directly computing \(c\) based on \(a\) and \(b\), the solution avoids unnecessary computations and narrows down the search space effectively.
   - The algorithm performs a simple numeric validation \(c^2 = a^2 + b^2\) after calculating \(c\), which ensures only valid triples are counted. This indirect validation (checking conditions post-calculation) keeps the process straightforward and avoids additional iterations.
   - Given that the maximum number of solutions correlates with the squares of numbers that are less than or equal to \(n\), this method is practical for the input size typically expected in competitive programming scenarios.

Overall, while there are other approaches to solving this problem, the straightforward nested loop with a mathematical condition gives a clear and easy-to-understand solution that is adequate for the constraints provided by the problem statement.
```

Runtime: undefined
Memory: 17764000
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
            for b in range(1, n + 1):
                # determine if it meets the requirements
                c = int(sqrt(a**2 + b**2 + 1))
                if c <= n and c**2 == a**2 + b**2:
                    res += 1
        return res
