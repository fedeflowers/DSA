"""
### Explanation of the Approach

The problem "Count Subarrays With Fixed Bounds" requires us to count the number of subarrays within a given list of integers `nums` that have all their elements between specified bounds `minK` and `maxK`, inclusive. The solution uses a single-pass method with a few key variables to track indices of interest in the array.

1. **Variable Initialization**: 
   - `res`: to store the total count of valid subarrays.
   - `bad_idx`: to store the index of the last element that is outside the bounds `[minK, maxK]`.
   - `min_idx`: to keep track of the last index where the element is `minK`.
   - `max_idx`: to track the last index where the element is `maxK`.

2. **Iterating through the Array**:
   - For each element `nums[r]`, check if it falls out of bounds (less than `minK` or greater than `maxK`). If so, update `bad_idx` to the current index `r`.
   - If the current element is equal to `minK`, update `min_idx`.
   - If the element equals `maxK`, update `max_idx`.
   
3. **Calculating Valid Subarrays**:
   - The number of valid subarrays that end at index `r` can be calculated as the difference between the smallest of `min_idx` and `max_idx`, and the last bad index `bad_idx`. Essentially, `min(min_idx, max_idx) - bad_idx` gives the count of subarrays that end at `r` and begin after the last bad element. The `max(0, ...)` ensures we don't end up with negative counts.

4. **Result**: 
   - The result `res` accumulates this count as we iterate through all elements.

### Time and Space Complexity Analysis

1. **Time Complexity**: 
   - The algorithm runs in O(N) time where N is the number of elements in `nums`. This is because we make a single pass through the array, performing constant-time operations for each element.

2. **Space Complexity**: 
   - The space complexity is O(1), as we use a constant amount of space for the variables (`res`, `bad_idx`, `min_idx`, `max_idx`) regardless of the input size.

### Why This Approach is Efficient

This approach is efficient for several reasons:

- **Single Pass**: It only needs one iteration over the input array, leading to an O(N) time complexity which is optimal for problems like this that require examining each element.
  
- **Memory Usage**: Employing just a few pointers results in constant space consumption, making it space-efficient.

- **Dynamic Tracking**: By maintaining indices for critical conditions (like the last bad index and the last occurrences of the minimum and maximum), the program effectively narrows down the valid starting points of the subarrays without needing to re-examine previously seen elements.

In summary, this solution effectively balances time and space complexity while providing a clear logic that leverages index tracking for efficient count calculations regarding fixed bounds in subarrays.

Runtime: undefined
Memory: 28788000
"""

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = min_idx = max_idx = -1
        for r in range(len(nums)):
            if not (minK <= nums[r] <= maxK):
                bad_idx = r
            if nums[r] == minK:
                min_idx = r
            if nums[r] == maxK:
                max_idx = r

            res += max(0, min(min_idx, max_idx) - bad_idx)

        return res
