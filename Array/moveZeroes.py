"""
## Explanation of the LeetCode Solution for "Move Zeroes"

### 1. Brief Explanation of the Approach

The solution to the "Move Zeroes" problem utilizes a two-pass approach to rearrange the elements of the list `nums` in place. The aim is to shift all non-zero elements to the start of the list while maintaining their relative order, and to move all zeros to the end of the list. 

- **First Pass**: The function iterates through the list. It maintains a variable `start_idx` that tracks the position at which the next non-zero element should be placed. Whenever a non-zero element is encountered, it is copied to the position indicated by `start_idx`, and `start_idx` is incremented. If a zero is encountered, a counter (`count_zeros`) is incremented instead.
  
- **Second Pass**: After all non-zero elements have been moved to the front of the list, the remaining positions (from `start_idx` to the end of the list) are filled with zeros using a reverse loop that starts from the end of the list.

Finally, the modified list has all non-zero elements at the beginning and all zeros at the end.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: The overall time complexity of this approach is O(n), where n is the length of the input list `nums`. This is because both passes through the list are linear in complexity; the first pass processes each element once, and the second pass processes the remaining elements, all in a direct manner.

- **Space Complexity**: The space complexity is O(1), as the algorithm only uses a fixed amount of extra space regardless of the input size. It uses a constant amount of additional variables (e.g., `start_idx` and `count_zeros`).

### 3. Why This Approach is Efficient

This approach is efficient for several reasons:

- **In-Place Modification**: The algorithm modifies the list in place without requiring any additional arrays or data structures, thus saving space.

- **Preservation of Order**: The solution maintains the relative order of non-zero elements, which is often a requirement in such problems.

- **Linear Time Complexity**: By using only two linear passes over the input list, the approach minimizes the total number of operations needed, making it scalable for larger input sizes.

- **Simple and Intuitive**: The use of clear variable names and straightforward logic makes the algorithm easy to understand and implement, which is advantageous for both learning and practical coding scenarios.

In summary, this two-pass approach efficiently addresses the problem while maintaining both time and space efficiency and preserving the order of the elements.

Runtime: undefined
Memory: 19064000
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # o un bubble sort O(n2), oppure, conto gli zero e sposto gli elementi prima? oppure sposto solo elementi prima
        # idea migliore, conto zeri e poi mi tengo index per mettere elementi non zero, alla fine gli zero li inserisco dalla fine
        start_idx = 0
        count_zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start_idx] = nums[i]
                start_idx += 1
            else:
                count_zeros += 1

        for i in range(len(nums)-1, len(nums) - count_zeros - 1, -1):
            nums[i] = 0

        return nums
