"""
```markdown
## Explanation of the "Container With Most Water" Solution

This solution aims to find the maximum area of water that can be contained by two lines represented in an array where the height of each line is given.

### 1. Brief Explanation of the Approach:

The approach utilizes the two-pointer technique. Here are the key steps:

- **Initialize Pointers**: Set two pointers, `l` (left pointer) starting at the beginning of the array (index 0) and `r` (right pointer) at the end of the array (last index).
  
- **Calculate Area**: The area formed between the two lines at positions `l` and `r` is calculated using the formula:
  
  \[
  \text{Area} = \min(\text{height}[l], \text{height}[r]) \times (r - l)
  \]
  
  This calculates the area of water that can be trapped between these two heights, where the limiting factor for the height is the shorter of the two lines.

- **Update Most Water**: Compare and update the maximum area (`most_water`) found so far.

- **Move Pointers**: Move the pointer that points to the shorter line:
  - If `height[l]` is less than `height[r]`, increment the left pointer `l` (i.e., move towards the right).
  - Else, decrement the right pointer `r` (i.e., move towards the left).
  
- **Repeat**: Continue the process until the left pointer meets the right one.

- **Return the Result**: Once the pointers meet, return the maximum area found.

### 2. Time and Space Complexity Analysis:

- **Time Complexity**: O(N)
  - The algorithm runs in linear time, where N is the number of elements in the input list. Each pointer moves at most N times (once for each direction), ensuring that every pair of points is evaluated efficiently without redundant comparisons.

- **Space Complexity**: O(1)
  - The space complexity is constant because the solution only uses a fixed amount of extra space for the pointers and the maximum area variable, regardless of the input size.

### 3. Why This Approach is Efficient:

This two-pointer technique is efficient for this problem for several reasons:

- **Reduction of Search Space**: Instead of considering every possible pair of lines (which would be a O(N^2) solution), this method strategically reduces the potential combinations by only moving the pointer corresponding to the shorter line.
  
- **Greedy Nature**: By moving the pointer of the shorter line, it aims to find potentially taller lines that might maximize the area, hence leading to quick convergence to the optimal solution.
  
- **Linear Iteration**: The method leverages a simple iteration over the array while dynamically calculating the required values, which is optimal for a problem of this nature.

Overall, this approach strikes a balance between simplicity and efficiency, making it a standard solution for the "Container With Most Water" problem.
```

Runtime: undefined
Memory: 28608000
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        most_water = 0
        while l < r:
            most_water = max(most_water, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return most_water
