"""
```markdown
# Solution Explanation for LeetCode "Two Sum II - Input Array Is Sorted"

## 1. Approach

The provided solution utilizes a two-pointer technique to find two numbers in a sorted array that sum up to a given target. The overall strategy is straightforward:

- **Initialization**: Two pointers, `left` and `right`, are initialized at the start and end of the `numbers` list, respectively.
  
- **Iteration**: A `while` loop runs as long as the `left` pointer is less than or equal to the `right` pointer:
  - Calculate the sum of the elements at the `left` and `right` pointers.
  - If this sum equals the `target`, the indices (adjusted to 1-based) are returned as the result.
  - If the sum is greater than the `target`, the `right` pointer is decremented to reduce the sum (move left).
  - If the sum is less than the `target`, the `left` pointer is incremented to increase the sum (move right).

By leveraging the sorted nature of the input array, the solution efficiently narrows down the search for the two required numbers.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The time complexity of this approach is O(N), where N is the number of elements in the `numbers` list. The algorithm makes a single pass through the list with the two pointers, adjusting their positions depending on the sum in relation to the target.

- **Space Complexity**: The space complexity is O(1) since no additional data structures are used that scale with the input size. Only a constant amount of extra space is required (for the pointers and the return list).

## 3. Efficiency of the Approach

This approach is efficient because:
- It eliminates the need for a nested loop (which would lead to O(N^2) time complexity) by taking advantage of the sorted property of the input array.
- By moving the pointers based on the comparison of the current sum with the target, it converges towards the solution quickly without unnecessary checks.
- The solution operates in linear time, making it suitable for large inputs while maintaining minimal additional memory usage.

Overall, the two-pointer technique used in this solution efficiently finds the indices of the two numbers whose sum equals the target while respecting the constraints provided by the sorted input.
```

Runtime: undefined
Memory: 20692000
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target: 
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
