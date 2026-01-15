"""
## Explanation of the Approach

The solution aims to calculate the maximum area of a square hole that can fit within a given grid, where horizontal barricades (`hBars`) and vertical barricades (`vBars`) limit the available space. The algorithm proceeds with the following steps:

1. **Sorting the Barricades**: The horizontal and vertical barricades are sorted. Sorting is essential to allow the algorithm to easily compute the maximum consecutive empty spaces between the barricades.

2. **Finding Maximum Consecutive Spaces**:
   - For horizontal barricades (`hBars`), the algorithm iterates through the sorted list to find the maximum number of consecutive rows without a barricade. This is determined by checking if each pair of consecutive barricades are directly adjacent. If they are, it increments a counter; if not, it resets the counter.
   - The maximum consecutive spaces found for horizontal barricades is stored in `cons_h`.
   - The same logic is applied to the vertical barricades (`vBars`), storing the result in `cons_v`.

3. **Calculating the Maximum Side Length**: The maximum side length of the square hole is obtained by taking the minimum of `cons_h + 1` and `cons_v + 1`. The `+1` accounts for the fact that if there are `k` consecutive empty spaces, the maximum width or height for a square would be `k + 1`.

4. **Returning the Area**: Finally, the area of the square hole, which is the side length squared, is returned.

## Time and Space Complexity Analysis

- **Time Complexity**:
  - Sorting the `hBars` list takes \(O(k \log k)\), where \(k\) is the number of horizontal barricades.
  - Sorting the `vBars` list takes \(O(l \log l)\), where \(l\) is the number of vertical barricades.
  - The two loops that find the maximum consecutive spaces in both lists take \(O(k)\) and \(O(l)\) respectively.
  - Therefore, the overall time complexity is \(O(k \log k + l \log l)\).

- **Space Complexity**:
  - The primary use of space comes from the input lists and the variables used for computation. Since no additional data structures proportional to input size are created, the space complexity is \(O(1)\) (considering that the input size is fixed and does not change).

## Efficiency of the Approach

This approach is efficient primarily due to the following reasons:

1. **Sorting Optimization**: Sorting both barricade lists allows for a linear scan to compute the maximum consecutive empty spaces effectively. Without sorting, the problem would require a more intricate method to find gaps, leading to higher time complexity.

2. **Direct Calculation of Consecutive Spaces**: Taking one pass through the sorted lists to find the maximum gaps avoids unnecessary computations, making the solution scalable as the inputs grow.

3. **Simple Arithmetic for Area**: The final calculation to retrieve the area is straightforward, ensuring that the algorithm remains efficient even for larger inputs.

Overall, through a combination of sorting and linear scanning, the solution achieves an optimal performance for the problem at hand.

Runtime: undefined
Memory: 19356000
"""

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        cons_h, cons_v = 1, 1
        curr = 1
        for i in range(len(hBars)-1):
            if hBars[i] + 1 == hBars[i+1]:
                curr += 1
            else:
                curr = 1
            cons_h = max(cons_h, curr)
        curr = 1
        for i in range(len(vBars)-1):
            if vBars[i] + 1 == vBars[i+1]:
                curr += 1
            else:
                curr = 1
            cons_v = max(cons_v, curr)

        l = min(cons_v + 1, cons_h + 1)
        return l * l
