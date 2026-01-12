"""
## Explanation of the Solution

### 1. Approach

The problem "Minimum Time Visiting All Points" involves calculating the minimum time required to visit a series of points in a 2D plane, starting from one point and moving to the next. The solution provided uses the concept of calculating the "Chebyshev distance" between two points, which is defined as the maximum of the absolute differences of their respective coordinates.

Here’s a brief overview of how the solution works:

- The function `minTimeToVisitAllPoints` takes a list of points as input.
- It initializes a variable `total_time` to keep track of the total time taken to visit all points.
- A loop iterates through each pair of consecutive points in the list:
  - For each pair of points `(x1, y1)` and `(x2, y2)`, it calculates the time to move from the first point to the second, which is determined by `max(abs(x1 - x2), abs(y1 - y2))`.
  - This value is then added to `total_time`.
  
Finally, the function returns the `total_time`, which is the total time needed to visit all the points sequentially.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - Here, N is the number of points in the input list. The algorithm makes a single pass through the list of points, processing each point pair once, leading to O(N) time complexity.
  
- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of extra space, irrespective of the input size. It only maintains a few integer variables (`total_time`, `x1`, `y1`, `x2`, `y2`), and does not use any additional data structures that scale with the input size.

### 3. Efficiency of the Approach

The approach is efficient for several reasons:

- **Optimal Distance Calculation**: The use of the maximum of the absolute differences of coordinates directly calculates the time needed to transition between two points in one step, aligning with the Chebyshev distance. This is optimal for determining movement in a grid where diagonal movement is as fast as horizontal or vertical movement.
  
- **Simple Iteration**: The algorithm processes each point in a single loop, making it straightforward and easy to follow. This ensures that the overhead of multiple nested loops or complex data structures is avoided.

- **Low Space Usage**: Since it operates with a fixed amount of space, it is very efficient in terms of memory usage, which is crucial for handling larger datasets.

Overall, this solution efficiently computes the minimum time to visit all points while maintaining simplicity and clarity in its implementation.

Runtime: undefined
Memory: 19404000
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            total_time += max(abs(x1 - x2), abs(y1 - y2))
        return total_time
