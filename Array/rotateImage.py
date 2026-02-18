"""
## Explanation of the LeetCode Solution for "Rotate Image"

### 1. Brief Explanation of the Approach
The solution uses two main steps to rotate the given `n x n` matrix (representing an image) 90 degrees clockwise:

1. **Transpose the Matrix**: The first step swaps the elements over the main diagonal of the matrix. This means that for each element at position `(i, j)`, it swaps it with the element at `(j, i)`. This step transforms the rows of the matrix into columns.

2. **Reverse Each Row**: After transposing the matrix, each row is reversed. Reversing the rows will adjust the positions of the elements to achieve a 90-degree clockwise rotation.

The operations are performed in place, meaning the original matrix is modified directly without using additional space for another matrix.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: The time complexity of the solution is \(O(n^2)\) where \(n\) is the number of rows (or columns, since it’s a square matrix). This is because we have two nested loops: one for transposing the matrix and one for reversing each row.

- **Space Complexity**: The space complexity is \(O(1)\). The algorithm modifies the matrix in place, so it doesn't use any additional data structures that grow with the size of the input.

### 3. Why This Approach is Efficient
This approach is efficient for several reasons:

- **In-Place Modification**: The algorithm operates in place, making it more space-efficient since it does not allocate additional memory based on the size of the input matrix.

- **Two Linear Passes**: The solution takes only two passes through the matrix, each consisting of a linear traversal. This is optimal for manipulating a matrix since it ensures that we are not performing unnecessary operations.

- **Simple Operations**: The operations involved (swapping elements and reversing lists) are straightforward and quick to execute, ensuring that the solution runs efficiently even for larger matrices.

Overall, this algorithm effectively utilizes the properties of matrix transposition and row reversal to achieve the desired result with minimal resource consumption.

Runtime: undefined
Memory: 19364000
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #swap over the diagonal and then reverse each row
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(r):
            matrix[i] = matrix[i][::-1]
            
        return matrix
                
        
