"""
```markdown
# Trapping Rain Water - Explanation

## 1. Brief Explanation of the Approach

The problem of trapping rain water involves calculating how much water can be stored between various elevations represented in an array (where each element corresponds to the height of a bar). 

The provided solution uses a two-pointer technique to solve the problem efficiently. The algorithm initializes two pointers, `l` (left) and `r` (right), at the beginning and the end of the height array, respectively. It also initializes two variables, `max_l` and `max_r`, which keep track of the maximum heights encountered from the left and the right side as the pointers move.

The solution operates as follows:
- It compares the heights at the left and right pointers:
  - If the height at the left pointer (`height[l]`) is less than or equal to the height at the right pointer (`height[r]`), then it means that the left pointer can potentially trap water:
    - Calculate the water trapped at this position using the formula: `max(min(max_l, max_r) - height[l], 0)` and update the total area.
    - Advance the left pointer (`l`).
  - If the height at the right pointer is less than the left, the same logic is applied from the right side:
    - Calculate and add the trapped water at the right position.
    - Move the right pointer (`r`) inward.

The process continues until the two pointers meet, at which point the total trapped water has been calculated.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)  
  In the worst case, the algorithm iterates through the height array once, where N is the number of elements in the array. The pointer adjustments and calculations inside the loop are all O(1) operations.

- **Space Complexity**: O(1)  
  The algorithm only uses a constant amount of extra space for variables (`l`, `r`, `total_area`, `max_l`, `max_r`), regardless of the input size.

## 3. Why This Approach is Efficient

This two-pointer technique is efficient for several reasons:
1. **Single Pass**: The algorithm only requires a single pass over the height array, making it much more efficient than a nested loop approach (which would have a time complexity of O(N^2)).
2. **Constant Space**: The algorithm achieves its goal using a constant amount of additional space, which is optimal for this problem.
3. **Adaptive**: By always comparing the left and right heights, it dynamically decides which side to explore next, ensuring that it considers only relevant heights for trapping water.

Overall, this approach balances time and space efficiency, making it suitable for large input sizes typical in competitive programming scenarios.
```

Runtime: undefined
Memory: 20928000
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total_area = 0
        max_l = max_r = -float("inf")
        while l < r:
            max_l = max(max_l, height[l])            
            max_r = max(max_r, height[r])
            if height[l] <= height[r]:
                total_area += max(min(max_l, max_r)-height[l], 0)
                l+= 1
            else:
                total_area += max(min(max_l, max_r)-height[r], 0)
                r-= 1
            
            
        return total_area
