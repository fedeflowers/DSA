"""
```markdown
# Explanation of the LeetCode Solution: "Maximum Subarray Sum With Length Divisible by K"

## 1. Brief Explanation of the Approach

The given solution utilizes the concept of prefix sums and modular arithmetic to efficiently find the maximum subarray sum with a length that is divisible by `k`. Here's the breakdown of the approach:

- **Prefix Sum**: We maintain a running sum called `curr_sum`, which keeps track of the cumulative sum of elements as we iterate through the array.
- **Modular Indexing**: We utilize a list `min_pre` of size `k` to store the minimum prefix sums at indices where the index modulo `k` gives the same remainder. This allows us to keep track of subarrays ending at different indices that could lead to a subarray length divisible by `k`.
- **Calculation**:
  - For each element in the `nums`, we calculate the current sum and determine the remainder `r` of the current index + 1 (to get the length of the subarray).
  - If we have previously recorded a minimum prefix sum for the same remainder `r`, we calculate the difference between the current sum and this minimum prefix sum. This difference gives us a candidate subarray sum that has length divisible by `k`.
  - We update the maximum sum `max_s` accordingly.
  - Finally, we update the `min_pre[r]` for the current cumulative sum.

The result is the maximum subarray sum found that satisfies the condition, or `0` if no such subarray exists.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n)  
  The solution iterates through the `nums` array only once, where `n` is the length of the array. The operations performed in each iteration (updating sums and checking conditions) are constant time operations.

- **Space Complexity**: O(k)  
  The space utilized is primarily for the `min_pre` list, which has a fixed size of `k`. Thus, regardless of the input size, the space complexity is determined by the value of `k`.

## 3. Why This Approach is Efficient

The efficiency of this approach hinges on the following aspects:

- **Single Pass**: By using a single iteration over the list, we minimize the time complexity. This is particularly advantageous for large arrays, as it avoids the need for nested loops (which can lead to O(n^2) complexity).
- **Modular Arithmetic**: By leveraging the properties of remainders and using prefix sums, we can efficiently find subarrays that meet the length condition. This smart use of modular arithmetic allows us to reduce the problem to constant-time lookups and updates in the `min_pre` list.
- **Immediate Return of Results**: The calculation of the maximum subarray sum is done on-the-fly. There are no additional iterations required after the main loop has completed, ensuring that we retrieve the result as quickly as possible.

The combination of these factors enables the solution to be both time-efficient and space-efficient, providing a significant advantage over more brute-force approaches.
```

Runtime: undefined
Memory: 40312000
"""

import math
from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # min_pre[r] stores the minimum prefix sum found at an index i where i % k == r
        min_pre = [math.inf] * k
        min_pre[0] = 0 # Base case: prefix sum 0 at index -1 (length 0)
        
        curr_sum = 0
        max_s = -math.inf
        
        for i, x in enumerate(nums):
            curr_sum += x
            
            # The current length is (i + 1). 
            # We look for a previous prefix sum at an index with the same remainder.
            r = (i + 1) % k
            
            if min_pre[r] != math.inf:
                max_s = max(max_s, curr_sum - min_pre[r])
            
            min_pre[r] = min(min_pre[r], curr_sum)
            
        return max_s if max_s != -math.inf else 0
