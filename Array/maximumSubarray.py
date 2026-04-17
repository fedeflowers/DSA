"""
```markdown
### LeetCode Solution Explanation for "Maximum Subarray"

#### 1. Brief Explanation of the Approach
The given solution uses an iterative approach to find the maximum sum of a contiguous subarray within the input array `nums`. 

- `curr_sum` is initialized to negative infinity to account for the scenario where all numbers in `nums` are negative.
- `res` also starts at negative infinity to track the maximum subarray sum found so far.
- The algorithm iterates through each number (`num`) in `nums`:
  - It updates `curr_sum` by adding the current number.
  - `res` is updated to be the maximum of its current value, `curr_sum`, and the current number `num`. This ensures that if a single number is greater than the `curr_sum`, it will reset `curr_sum` to that number.
  - If `num` is greater than `curr_sum`, it indicates that starting a new subarray from the current number may yield a higher sum, hence `curr_sum` is reset to `num`.
This continues until all elements of the array have been processed, and finally, `res` contains the maximum subarray sum.

#### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array `nums`. The algorithm makes a single pass through the array, processing each element exactly once.
- **Space Complexity**: O(1). The solution uses a constant amount of space for a few integer variables (`curr_sum` and `res`) and does not allocate new data structures based on input size.

#### 3. Why This Approach is Efficient
The efficiency of this approach lies in the use of a single pass through the array while only maintaining a few variables, thus minimizing both time and space complexity. The idea of resetting `curr_sum` when a single number is found to be greater than it ensures that we keep track of the best possible contiguous subarray sum dynamically. This efficient in-place tracking allows for immediate consideration of new potential subarray sums without needing to check all possible subarrays (which would lead to a higher time complexity).

By focusing on cumulative sums and dynamically resetting the starting point of the subarray, we achieve optimal performance suitable for large inputs.
```

Runtime: undefined
Memory: 31312000
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -float("inf")
        res = -float("inf")
        for num in nums:
            print(curr_sum)
            curr_sum = curr_sum + num
            res = max(res, curr_sum, num)
            if num > curr_sum:
                curr_sum = num #restart
        return res
                
                
            
