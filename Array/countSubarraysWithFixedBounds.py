"""
## Explanation of LeetCode Solution for "Count Subarrays With Fixed Bounds"

### 1. Approach

The problem "Count Subarrays With Fixed Bounds" requires counting the number of contiguous subarrays in an array that contain at least one instance of a given minimum value (`minK`) and at least one instance of a given maximum value (`maxK`). The solution employs a single-pass method through the array to track the necessary indices and calculate valid subarrays.

Here's a breakdown of the approach:

- **Initialization**: 
  - `res` is initialized to zero, which will hold the count of valid subarrays.
  - `bad_idx` marks the last index where an element outside the bounds `(minK, maxK)` was found. 
  - `min_idx` and `max_idx` are initialized to -1 and will store the indices of the last occurrences of `minK` and `maxK`, respectively.

- **Iteration**: 
  - The solution iterates through the array with `enumerate`, getting both the index `i` and the value `num`.
  - For each element:
    - If `num` is not within the valid bounds (i.e., not between `minK` and `maxK`), `bad_idx` is updated to the current index `i`.
    - If `num` is equal to `minK`, `min_idx` is updated to the current index.
    - If `num` is equal to `maxK`, `max_idx` is updated to the current index.
  - For each element, the valid subarrays ending at index `i` can be counted from the maximum of the last valid indices of `minK` and `maxK`, minus the last invalid index `bad_idx`.

- Finally, the result `res` is returned, representing the total count of valid subarrays found.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: 
  - The time complexity of the solution is O(N), where N is the length of the input array `nums`. This is because the solution iterates through the array in a single pass.

- **Space Complexity**: 
  - The space complexity of the solution is O(1) since it uses a constant amount of extra space regardless of the input size. Only a few integer variables are maintained for indices and count.

### 3. Efficiency of the Approach

This approach is efficient for several reasons:

- **Single Pass**: By performing only one pass through the array, the solution minimizes the number of iterations required, making it suitable for larger input sizes.

- **Constant Space Usage**: It achieves the goals using a fixed number of variables, thus preventing overhead from using additional data structures.

- **Direct Index Tracking**: By maintaining indices of the last occurrences of `minK`, `maxK`, and bad elements, it effectively counts valid subarrays without needing nested loops to generate all possible subarrays explicitly, which would be computationally expensive.

Overall, this method combines clarity and performance, making it an optimal solution for the problem at hand.

Runtime: undefined
Memory: 28864000
"""

class Solution:
    def countSubarrays(self, nums, minK, maxK):
        res = 0
        bad_idx = min_idx = max_idx = -1
        
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = i
            if num == minK:
                min_idx = i
            if num == maxK:
                max_idx = i
                
            res += max(0, min(min_idx, max_idx) - bad_idx)
            
        return res
