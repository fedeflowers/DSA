"""
```markdown
# Explanation of the LeetCode Solution for "Rotate Image"

## 1. Brief Explanation of the Approach

The problem requires rotating a given N x N matrix (2D list) 90 degrees clockwise in-place. The solution uses a two-step approach:

1. **Transpose the Matrix**: The first step involves transposing the matrix. Transposing means converting all the rows of the matrix into columns and vice versa. This is accomplished using nested loops, where each element at position `(i, j)` is swapped with the element at position `(j, i)`. This effectively flips the matrix over its diagonal.

2. **Reverse Each Row**: After transposing, the next step is to reverse each row of the matrix. This step aligns the transposed elements to create the final rotated structure. The reversal is done using Python's slicing method `matrix[i][::-1]`, which efficiently reverses the list in place.

Overall, the two operations together achieve the effect of a 90-degree rotation.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The transposition process requires visiting each element in the matrix exactly once, resulting in O(N^2) time complexity, where N is the number of rows (or columns) in the NxN matrix.
  - Similarly, reversing each row also takes O(N^2) time since we visit each element in the matrix again.
  - Therefore, the overall time complexity is O(N^2).

- **Space Complexity**: 
  - The algorithm modifies the matrix in-place and does not utilize any additional data structures that grow with input size. Thus, the space complexity is O(1), as the changes can be made directly within the original matrix without needing extra storage proportional to N.

## 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **In-place Modification**: The solution does not create any additional copies of the matrix, which conserves memory and optimizes space usage.
- **Two-pass Algorithm**: By utilizing both transposition and row reversal, the algorithm effectively transforms the matrix with minimal iteration, making it faster than approaches that might involve creating intermediate matrices.
- **Simplicity**: The logic behind transposing and reversing is intuitive and straightforward, making the implementation clear and easy to understand.

Overall, this approach effectively balances time efficiency and space optimization, making it suitable for the constraints typically posed by matrix rotation problems.
```

Runtime: undefined
Memory: 19360000
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(rows):
            matrix[i] = matrix[i][::-1]
            
        
