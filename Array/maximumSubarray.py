"""
# Explanation of the LeetCode Solution for "Maximum Subarray"

## 1. Approach Explanation

The provided solution implements a variation of the Kadane's Algorithm to find the maximum sum of a contiguous subarray from the input list `nums`. The main idea is to traverse through the elements of the array while maintaining a running sum (`curr_sum`) of the current subarray. Here’s how the code works:

- **Initialization**: We start with two variables, `curr_sum` and `res`, both initialized to negative infinity to handle cases where all elements could be negative. 

- **Iterate through the array**: For each number (`num`) in the list:
  - Update `curr_sum` by adding the current number to it.
  - Update `res` to the maximum value among `res`, `curr_sum`, and the current number `num`. This accounts for cases where starting a new subarray at the current number might yield a higher sum.
  - If the current number is greater than the current sum (`curr_sum`), we restart `curr_sum` with the current number, indicating that a new subarray should begin from this number.

- **Return Result**: After processing all numbers, `res` will contain the maximum sum of any contiguous subarray.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -float("inf")
        res = -float("inf")
        for num in nums:
            curr_sum = curr_sum + num
            res = max(res, curr_sum, num)
            if num > curr_sum:
                curr_sum = num #restart
        return res
```

## 2. Time and Space Complexity Analysis

- **Time Complexity**: The algorithm runs in O(n), where n is the number of elements in the input list `nums`. This is because it processes each element in the list exactly once in a single loop.

- **Space Complexity**: The space complexity is O(1). The algorithm uses a fixed amount of extra space for the variables `curr_sum` and `res`, regardless of the input size.

## 3. Efficiency of the Approach

This approach is efficient due to the following reasons:

- **Single Pass**: By processing each element of the array in a single pass (O(n)), we avoid the need for nested loops that could lead to O(n^2) time complexity, especially crucial for large arrays.

- **Constant Space**: The use of only a couple of variables for tracking the current sum and the result minimizes memory usage, making it suitable for problems with potential large input sizes.

- **Handling Edge Cases**: The initialization with negative infinity allows the solution to correctly handle cases where all elements are negative, ensuring it accurately finds the maximum contiguous subarray sum (which, in such cases, will be the largest single element).

Overall, this implementation balances time efficiency and space efficiency, making it an optimal solution to the "Maximum Subarray" problem.

Runtime: undefined
Memory: 31588000
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -float("inf")
        res = -float("inf")
        for num in nums:
            curr_sum = curr_sum + num
            res = max(res, curr_sum, num)
            if num > curr_sum:
                curr_sum = num #restart
        return res
                
                
            
