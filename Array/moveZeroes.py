"""
## Explanation of the "Move Zeroes" Solution

### 1. Brief Explanation of the Approach
The approach taken in this solution is to modify the input list `nums` in-place by moving all the non-zero elements to the front while maintaining their relative order, and then placing all zeroes at the end of the list.

The logic can be broken down into two main passes through the list:
- **First Pass**: This pass iterates through the `nums` list. For every non-zero element encountered, it is placed in the position indicated by `start_idx`, which keeps track of where the next non-zero element should go. After placing a non-zero element, `start_idx` is incremented.
- **Second Pass**: After all non-zero elements have been moved to the front, the second pass fills the remaining positions in the list with zeroes. This starts from the `start_idx` to the end of the list.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the `nums` list. This is because we are making two passes through the array: one to move the non-zero elements and another to fill in the zeroes. Each pass takes linear time.
- **Space Complexity**: O(1). The solution modifies the input list in-place without using any additional data structures that scale with input size. The only additional variables used (e.g., `start_idx`) take up constant space.

### 3. Why This Approach is Efficient
This approach is efficient for several reasons:
- **In-Place Modification**: The algorithm modifies the input array without needing any extra space for another array. This is useful in scenarios where memory usage is a concern.
- **Maintaining Order**: By keeping track of the position for the next non-zero element, the algorithm ensures that the relative order of non-zero elements is preserved, which is often required in such problems.
- **Single Pass for Filling Zeroes**: Instead of counting zeroes during the first pass and then performing additional operations to place them, this method simply uses `start_idx` to determine where to fill zeroes, allowing it to be straightforward and efficient.

By utilizing these steps, the solution effectively handles the requirement to move all zeroes to the end while ensuring that non-zero elements maintain their original order.

Runtime: undefined
Memory: 18988000
"""

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # o un bubble sort O(n2), oppure, conto gli zero e sposto gli elementi prima? oppure sposto solo elementi prima
#         # idea migliore, conto zeri e poi mi tengo index per mettere elementi non zero, alla fine gli zero li inserisco dalla fine
#         start_idx = 0
#         count_zeros = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[start_idx] = nums[i]
#                 start_idx += 1
#             else:
#                 count_zeros += 1

#         for i in range(len(nums)-1, len(nums) - count_zeros - 1, -1):
#             nums[i] = 0

#         return nums

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # with only idx
        start_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start_idx] = nums[i]
                start_idx += 1

        for i in range(start_idx, len(nums)):
            nums[i] = 0

        return nums
