"""
```markdown
## Explanation of the "Count Square Sum Triples" Solution

### 1. Approach Explanation
The goal of the problem is to count the number of unique triples \((a, b, c)\) such that \(a^2 + b^2 = c^2\) and \(1 \leq a, b, c \leq n\).

In the given solution:
- We first create an array called `squares` that holds the squares of numbers from 1 up to \(n\).
- A set called `fast_sq` is generated from the `squares` list to enable efficient lookups.
- We then use a double loop to iterate through pairs of squares. For each pair \((i, j)\), we check if their sum exists in the `fast_sq` set.
- If it does, it means there exists a third integer \(c\) such that \(a^2 + b^2 = c^2\), and we increment the result `res` by 2 to account for the combinations \((a, b)\) and \((b, a)\) since they can form the same triple.

The final result is returned, which represents the total number of unique triples that satisfy the equation.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The outer loop runs \(O(n^2)\) and the inner loop runs \(O(1)\) on average due to the set lookup for `fast_sq`. Thus, the complete solution has a time complexity of \(O(n^2)\).
- **Space Complexity**: The space required for the `squares` list and the set `fast_sq` is \(O(n)\), since they store square values for numbers from \(1\) to \(n\).

### 3. Efficiency of the Approach
This approach is efficient because:
- It leverages a set for constant time complexity lookups, which significantly speeds up the process of checking if a sum of two squares is also a square root of some integer.
- By iterating over pairs only once and generating combinations logically (ensuring uniqueness through the \(i, j\) loop), the solution effectively counts valid triples without redundant checks, avoiding a more naive \(O(n^3)\) solution.
- The use of a double loop is balanced and still manageable due to the constraints set by \(n\) while ensuring that performance remains practical for the problem's limits.
```


Runtime: undefined
Memory: 17752000
"""

class Solution:
    def countTriples(self, n: int) -> int:
        #brute force O(n**2)
        squares = []
        res = 0
        for i in range(1, n + 1):
            squares.append(i**2)

        fast_sq = set(squares)

        for i in range(len(squares)):
            for j in range(i+1, len(squares)):
                if squares[i] + squares[j] in fast_sq:
                    res += 2

        return res
