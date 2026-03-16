"""
## Explanation of the "Container With Most Water" Solution

### 1. Brief Explanation of the Approach

The solution uses a two-pointer technique to efficiently find the maximum area of water that can be trapped between two vertical lines that are represented by the heights in the `height` list. The idea is to initialize two pointers, one at the start (`l`) and one at the end (`r`) of the height list. 

- **Calculate Width and Height**: The width between the two pointers is the difference `r - l`, and the height is determined by the shorter of the two heights at these pointers (`min(height[l], height[r])`).
- **Calculate Area**: The area formed by these two lines as boundary is calculated as `h * width`.
- **Update Maximum Area**: Keep track of the maximum area encountered so far.
- **Pointer Adjustment**: To potentially find a greater area, the algorithm moves the pointer pointing to the shorter line inward (i.e., if `height[l] < height[r]`, increment `l`. Otherwise, decrement `r`). This is because moving the taller line wouldn't help to increase the height and only reduces the width.

This process continues until the two pointers meet, ensuring that all potential container combinations are evaluated efficiently.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The algorithm runs in O(N) time, where N is the number of elements in the `height` array. This is because each pointer (`l` and `r`) traverses the list only once.
  
- **Space Complexity**: The solution uses O(1) space since it only utilizes a fixed amount of extra space for the pointers and some variables (e.g., `max_water`, `width`, and `h`). It does not utilize any additional data structures that grow with input size.

### 3. Why This Approach is Efficient

The two-pointer technique is efficient for this problem due to the following reasons:

- **Optimal Pair Coverage**: By starting from both ends of the array and moving towards the center, the algorithm ensures that it checks all possible pairs that can form a container. This maximizes the chances of finding the maximal area without redundantly evaluating all pairs (which would be O(N^2)).
  
- **Height Limitation Handling**: Adjusting the pointer of the shorter line allows the algorithm to discard suboptimal configurations quickly since the water level is limited by the shorter of the two lines. 

- **Direct Calculation**: All necessary information (width and height) for calculating the area can be derived from the pointer positions, making the solution simple and elegant while maintaining efficiency.

In summary, this approach effectively balances between thoroughness and efficiency, resulting in a solution that scales well with input size.


Runtime: undefined
Memory: 29816000
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            # Width is the distance between pointers
            width = r - l
            # Height is limited by the shorter bar
            h = min(height[l], height[r])
            
            max_water = max(max_water, h * width)
            
            # Move the pointer of the shorter bar
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_water
