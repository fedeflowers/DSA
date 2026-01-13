"""
```markdown
# Explanation of the LeetCode Solution for "Separate Squares I"

## 1. Approach
The problem "Separate Squares I" involves finding a horizontal line (y = line) that divides a set of squares into two parts such that the areas of the squares above the line and below the line are as close as possible. 

The solution employs a binary search strategy to efficiently locate the optimal line that minimizes the absolute difference in areas between the two divisions. The process can be outlined as follows:

- The function `calculate_area` takes a specific line and computes the total area of the squares above and below that line.
   - For each square characterized by its coordinates (x, y) and edge length e:
     - If the square is entirely above the line, its area contributes to the `above` total.
     - If the square is entirely below the line, its area contributes to the `below` total.
     - If the square straddles the line, the areas above and below the line are calculated based on the amount of the square that lies above or below the line.
- The binary search operates between the minimum (`lo`) and maximum (`hi`) y-coordinates of the squares. The precision is set to a small value (1e-5) to ensure a high degree of accuracy.
- In each iteration of the binary search, the middle point `mid` is calculated, and the areas above and below this line are determined. Based on whether the area above is greater or less than that below, the search space is adjusted.
- The final result, representing the optimal division line, is returned as the average of `lo` and `hi` at the termination of the loop.

## 2. Time and Space Complexity
**Time Complexity:**
- The binary search performs O(log(range)) iterations where `range` is the difference between `hi` and `lo`.
- In each iteration, the algorithm processes all `N` squares to compute the areas, resulting in O(N) time for each iteration.
- Thus, the overall time complexity is O(N * log(range)), where N is the number of squares.

**Space Complexity:**
- The space complexity is O(1) since the algorithm only uses a constant amount of additional space, regardless of the input size (the sizes of the input squares and other scalars).

## 3. Efficiency of the Approach
This approach is efficient due to the use of binary search combined with a linear scan of the squares, which significantly reduces the number of calculations required compared to a naive brute-force method that would directly check every possible horizontal line. The precision requirement ensures that the result is sufficiently accurate, making the binary search suitable for this problem. Additionally, since the calculations for areas are straightforward and can be performed in a single pass through the list of squares, this balances the computational load effectively.
```

Runtime: undefined
Memory: 48284000
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate_area(squares, line):
            above = 0
            below = 0
            for x, y, e in squares:
                if y >= line:
                    above += e * e
                elif y + e <= line:
                    below += e * e
                else:
                    above_h = y + e - line
                    below_h = line - y
                    above += above_h * e
                    below += below_h * e
            return above, below

        precision = 1e-5
        hi = max(y + e for _, y, e in squares)
        lo = min(y for _, y, _ in squares)

        #brute force
        # best_y = min_line
        # min_diff = float('inf')

        # y = min_line
        # step = 1e-5
        # while y <= max_line:
        #     above, below = calculate_area(squares, y)
        #     diff = abs(above - below)
        #     if diff < min_diff:
        #         min_diff = diff
        #         best_y = y
        #     y += step

        # return best_y


        #binary search
        while hi - lo > precision:
            mid = (lo + hi) / 2
            above, below = calculate_area(squares, mid)

            if above > below:
                lo = mid
            else:
                hi = mid

        return (lo + hi) / 2
