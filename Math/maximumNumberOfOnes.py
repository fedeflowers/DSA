"""
```markdown
# Explanation of the "Maximum Number of Ones" Solution

## 1. Brief Explanation of the Approach

The provided solution aims to determine the maximum number of `1`s that can be placed in a 2D grid of dimensions `width` x `height`, where the `1`s are arranged in repeating blocks of size `sideLength` x `sideLength`. We have a restriction on the number of `1`s being added, denoted by `maxOnes`. 

### Step-by-Step Process:

1. **Calculate Weights**: 
   - For each cell `(r, c)` in a `sideLength` x `sideLength` block, the algorithm computes how many times that specific cell will appear in the entire grid based on its row and column position. 
   - The weights are calculated using:
     - `num_rows = (height - 1 - r) // sideLength + 1` indicates how many times row `r` will be repeated within the grid.
     - `num_cols = (width - 1 - c) // sideLength + 1` indicates how many times column `c` will be repeated.
   - The overall contribution (weight) of each cell is the product of the row and column repetitions: `num_rows * num_cols`.

2. **Sort Weights**: 
   - Once all weights are determined for each cell in the block, they are sorted in descending order. This allows us to easily identify which cells can contribute the most `1`s.

3. **Select Top Weights**: 
   - The final step involves summing the top `maxOnes` values from the sorted weights. This sum represents the maximum number of `1`s that can be placed in the grid, constrained by the `maxOnes` limit.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The algorithm involves nested loops iterating through a `sideLength` x `sideLength` grid, resulting in a complexity of `O(sideLength^2)` for calculating weights. Sorting the weights takes `O(n log n)`, where `n` is the number of weights (which equals `sideLength^2`).
  - Thus, the overall time complexity is:
    \[
    O(sideLength^2 \log(sideLength^2))
    \]
  
- **Space Complexity**: 
  - The space required is predominantly for storing the weights, which has a size of `O(sideLength^2)`. Therefore, the space complexity is:
    \[
    O(sideLength^2)
    \]

## 3. Why This Approach is Efficient

This approach efficiently utilizes the repeating structure of the grid formed by `sideLength` x `sideLength` blocks. By calculating the contribution of each block cell to the grid once and leveraging the sorted weights, the algorithm minimizes redundant calculations. 

- The use of mathematical calculations to determine repetitions avoids the need to construct and analyze the entire grid, which could be time and space-intensive. 
- Sorting the weights ensures that the algorithm can quickly access the highest contributing cells, thereby minimizing computational overhead when selecting the top `maxOnes`.

Overall, the method efficiently navigates through the problem parameters, resulting in a solution that scales effectively with inputs.
```

Runtime: undefined
Memory: 17704000
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

                # fai prima le righe e poi le colonne, height -1 perchè gli indici partono da 0,
                #  - r perchè a l'indice da cui inizi a contare, quindi ci sono height - 1 - r posti dopo il primo,
                #  //sidelegth è quanti ce ne stanno in questi spazi, e il + 1 finale è per contare l'indice 0
                num_rows = (height - 1 - r) // sideLength + 1 
                
                # Calculate how many times col 'c' repeats in the total width
                num_cols = (width - 1 - c) // sideLength + 1
                
                # Total occurrences of this cell is row_repeats * col_repeats
                weights.append(num_rows * num_cols)
        
        # Sort weights in descending order to pick the most frequent positions
        weights.sort(reverse=True)
        
        # Sum the top 'maxOnes' weights
        return sum(weights[:maxOnes])



