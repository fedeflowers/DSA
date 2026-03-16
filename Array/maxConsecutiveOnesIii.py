"""
```markdown
### Explanation of the Approach

The problem "Max Consecutive Ones III" is about finding the longest subarray of 1's in a binary array, where you can flip at most `k` zeros into 1's.

The given solution employs the "sliding window" technique to efficiently find this maximum length. Here's a breakdown of the approach:

1. **Initialization**: 
   - `left` pointer is initialized to the start of the array.
   - `zerosCount` keeps track of the number of zeros in the current window.
   - `maxLength` is used to store the maximum length of a valid subarray found so far.

2. **Expanding the Window**:
   - A `for` loop iterates over the array using a `right` pointer.
   - Whenever a zero is encountered (`nums[right] == 0`), `zerosCount` is incremented.

3. **Contracting the Window**:
   - If the count of zeros exceeds `k`, the left side of the window is contracted (the `left` pointer is moved to the right) until we have at most `k` zeros in the current window. 
   - While moving the `left` pointer, if a zero is skipped, `zerosCount` is decremented.

4. **Updating Maximum Length**:
   - After adjusting the window, the current length of the window (`right - left + 1`) is calculated and `maxLength` is updated if the current length is larger.

5. **Result**: 
   - The function ultimately returns `maxLength`, which represents the length of the longest subarray containing at most `k` zeros.

### Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - The `right` pointer makes a single pass through the array, going from left to right. The `left` pointer only advances, never moving back. Thus, both pointers together traverse the entire array in linear time.

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of space for the variables (`left`, `zerosCount`, `maxLength`, etc.) and does not use any additional data structures that grow with the input size.

### Why This Approach is Efficient

This sliding window approach is efficient because it minimizes the number of operations required to check for valid subarrays. Instead of checking every possible subarray (which would lead to an O(N^2) solution), it maintains a dynamic window that expands and contracts based on the condition regarding zeros. This allows us to effectively keep track of the longest valid subarray in linear time and with constant space, which is optimal for this problem type.
```

Runtime: undefined
Memory: 22248000
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zerosCount = 0
        maxLenght = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerosCount += 1
            while zerosCount > k:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            currentLenght = right - left + 1
            maxLenght = max(currentLenght, maxLenght)
        return maxLenght
