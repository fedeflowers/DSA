"""
## Explanation of the Solution

### 1. Brief Explanation of the Approach
The problem "Maximum Number of Ones" aims to determine the maximum number of ones that can be placed in a grid defined by its `width`, `height`, and a repeating square block of size `sideLength x sideLength`. You are allowed to place at most `maxOnes` ones in this grid.

The solution involves the following steps:

- **Weight Calculation**: For each cell in the `sideLength x sideLength` block, the algorithm computes how often that cell will be repeated in the overall grid when the block is tiled across the entire width and height of the grid. This is captured in a weight array, where each element corresponds to the number of times a particular cell will contribute to the grid.
  
- **Weight Sorting**: After calculating the weights for all cells in the block, the weights are sorted in descending order. This allows for easily selecting the cells that contribute the most ones to the grid.

- **Optimal Selection**: Finally, the algorithm sums the weights of the top `maxOnes` positions, which yields the maximum number of ones that can be placed in the grid under the constraints specified.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: 
  - The nested loops for calculating weights run in `O(sideLength^2)` since both rows (`r`) and columns (`c`) iterate through `sideLength`. 
  - Sorting the weights array will take `O(n log n)`, where `n` is the number of cells in the grid (which equates to `sideLength^2`).
  - Thus, the overall time complexity of the solution is `O(sideLength^2 log(sideLength^2))`.

- **Space Complexity**: 
  - The main space usage comes from the `weights` list, which has `sideLength^2` elements, resulting in a space complexity of `O(sideLength^2)`.

### 3. Why This Approach is Efficient
This approach is efficient because it:
- Focuses directly on the contributions of each cell in the small repeating block rather than examining every cell in the entire grid, which would lead to poor performance with larger dimensions.
- The use of sorting allows for quickly selecting the cells with the highest contributions, ensuring that we maximize the total number of ones placed in a controlled manner, balancing the precision of contributions against the upper limit imposed by `maxOnes`.
- The calculations are based entirely on the mathematical properties of the grid and the tiling aspect, thereby ensuring that the algorithm runs in polynomial time relative to the block size rather than the potentially much larger grid size. This leads to scalability in handling larger grids efficiently.

By utilizing these methodologies, the solution effectively calculates the maximum number of ones without the need to simulate the entire grid directly.

Runtime: undefined
Memory: 18160000
"""

class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        # List to store the repetition count (weight) of each position in the sideLength x sideLength block
        weights = []
        
        # Loop through the fundamental block
        for r in range(sideLength):
            for c in range(sideLength):
                # Calculate how many times row 'r' repeats in the total height
                # Formula: (total_rows - 1 - current_row) // step + 1
                num_rows = (height - 1 - r) // sideLength + 1
                
                # Calculate how many times col 'c' repeats in the total width
                num_cols = (width - 1 - c) // sideLength + 1
                
                # Total occurrences of this cell is row_repeats * col_repeats
                weights.append(num_rows * num_cols)
        
        # Sort weights in descending order to pick the most frequent positions
        weights.sort(reverse=True)
        
        # Sum the top 'maxOnes' weights
        return sum(weights[:maxOnes])

