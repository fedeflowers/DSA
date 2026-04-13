"""
```markdown
## Explanation of the Solution for "Minimum Distance to the Target Element"

### 1. Approach Explanation

The given solution uses a two-pointer technique to find the minimum distance from a given starting index to the nearest occurrence of the specified target value in the `nums` list. The algorithm proceeds as follows:

- Initialize two pointers `l` and `r` to `start`, one for searching towards the left (`l`) and the other towards the right (`r`).
- Iteratively check both sides:
  - If `l` (left pointer) is within bounds (i.e., `l >= 0`), check if `nums[l]` is equal to `target`. If it is, the distance is calculated as `start - l`, and this value is returned.
  - If `r` (right pointer) is within bounds (i.e., `r < n`), check if `nums[r]` is equal to `target`. If it is, the distance is calculated as `r - start`, and this value is returned.
- Both pointers are then moved closer to the limits of `nums`: decrement `l` to check further left and increment `r` to check further right.
- The loop continues until either a target is found or the pointers exceed the bounds of the array.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N), where N is the length of the `nums` list. In the worst-case scenario, we may need to move both pointers to the ends of the list before finding the target. This means we might check every element at most once.
  
- **Space Complexity**: O(1). The algorithm only uses a fixed amount of space for the pointers `l` and `r`, irrespective of the input size.

### 3. Efficiency of the Approach

This approach is efficient because:
- It leverages a linear search with two pointers that simultaneously check both sides of the starting index for the closest target. This results in a straightforward and effective way to find the target without needing additional space for extra data structures or complex logic.
- The algorithm exits as soon as it finds the nearest target, which can occasionally save checks if the target is located close to the starting index.
- The simplicity of the pointer manipulation provides a clear and clean implementation, with minimal overhead in terms of both time and space.

Overall, this solution effectively finds the minimum distance to the target element in an optimal manner.
```

Runtime: undefined
Memory: 19296000
"""

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        # 1 on the right, 1 on the left
        r = l = start
        while l >= 0 or r < n:
            if l >= 0 and nums[l] == target:
                return start - l
            if r < n and nums[r] == target:
                return r - start
            
            l-=1
            r+=1
        
