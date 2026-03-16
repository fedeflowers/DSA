"""
# Explanation of the Maximal Rectangle Solution

## 1. Brief Explanation of the Approach

The solution to the "Maximal Rectangle" problem utilizes a histogram-based approach to efficiently compute the largest rectangle that can be formed in a binary matrix filled with '0's and '1's. Here's a breakdown of how the approach works:

- **Matrix Interpretation**: Each row of the binary matrix represents a base for a histogram. The value of `heights[i]` at each column `i` keeps track of the height of consecutive '1's in that column, treating the '1's as heights of histogram bars.

- **Building Heights**: As we iterate through each row of the matrix:
  - For each position in the row, we update the `heights` array. If the current cell contains '1', we increment the height of that column. If it contains '0', we reset that height to 0.
  
- **Calculating Maximal Rectangle**: After updating the `heights` for the current row, we use a stack to calculate the maximal rectangle area that can be formed using the histogram represented by `heights`:
  - We iterate through each column and maintain a stack that helps track the indices of the heights in a non-decreasing order.
  - For each column, if the current height is less than the height at the top of the stack, we pop from the stack and calculate the area based on the height of the popped index and the width determined by the current index and the top of the stack after popping.
  
- **Area Calculation**: The area for each popped height is calculated as \(h \times w\), where \(h\) is the popped height and \(w\) is the width determined by the indices from the stack.

- The maximum area found during this process is recorded and returned.

## 2. Time and Space Complexity Analysis

### Time Complexity
- The overall time complexity of this solution is \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns in the matrix. This is because we process each cell in the matrix once to update heights and subsequently use a single pass (through the `heights` array) to compute maximal rectangles.

### Space Complexity
- The space complexity is \(O(n)\), which is used for the `heights` array and an auxiliary stack of size at most \(n + 1\).

## 3. Why This Approach is Efficient

The efficiency of this approach stems from its use of a linear scan combined with a stack to handle the histogram area calculation in a manner similar to the "Largest Rectangle in Histogram" problem, with the added benefit of a scalable method to update heights dynamically as we move through the rows of the matrix.

- **Dynamic Height Calculation**: Instead of recalculating heights from scratch for every row, we incrementally update them, which saves time.

- **Stack Usage**: The stack technique effectively reduces the needed time for area calculations to linear time, eliminating the need for nested loops to find the boundaries for each height.

Overall, the use of a linear approach with stack optimizations enables handling potentially large matrices efficiently, making this solution both optimal and elegant.

Runtime: undefined
Memory: 24436000
"""

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
