"""
```markdown
# Explanation of the LeetCode Solution for "Maximum Product Subarray"

## 1. Approach Explanation

The solution uses an iterative approach to determine the maximum product of a contiguous subarray. The key idea is to maintain two variables, `currMax` and `currMin`, which track the maximum and minimum product that can be achieved ending at the current element. This is crucial because a negative number can turn the smallest product (which would be negative) into the largest product when multiplied.

Here's how the algorithm works:

- Initialize `currMin` and `currMax` to 1, and set the result `res` to the first element in the input array `nums`.
- Iterate through each element `el` in `nums`:
  - If `el` is 0, reset `currMin` and `currMax` to 1 and update `res` to be the maximum of `res` and `el` (which is 0).
  - If `el` is not 0:
    - Calculate a temporary product `tmp` as `currMax * el`.
    - Update `currMax` to be the maximum among `tmp`, `currMin * el`, and `el`, which represents the maximum product that can end with `el`.
    - Update `currMin` to be the minimum among `tmp`, `currMin * el`, and `el`, which represents the minimum product that can end with `el`.
    - Update `res` to be the maximum of `currMax` and the previously recorded `res`.

At the end of the iteration, `res` contains the maximum product of any contiguous subarray.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - The algorithm iterates through the array `nums` once, making a single pass through the elements. Here, N is the number of elements in `nums`.

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of space (only a few integer variables) irrespective of the size of the input array.

## 3. Efficiency of the Approach

This approach is efficient due to the following reasons:

- **Single Pass**: The solution completes in a single traversal of the input array, which minimizes time complexity.
- **Handling Both Positive and Negative Numbers**: By keeping track of both the maximum and minimum products, the algorithm handles negative numbers seamlessly, as multiplying two negative numbers results in a positive product.
- **Resetting on Zero**: The strategy of resetting the counters when a zero is encountered allows the algorithm to effectively skip subarrays that cannot yield a product greater than zero.
- **Constant Space Usage**: Using only a few variables means that this approach is memory efficient, making it suitable for large input sizes.

This efficient use of space and time makes the algorithm suitable for competitive programming and real-world application scenarios where performance is critical.
```

Runtime: undefined
Memory: 19908000
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        res = nums[0]
        for el in nums:
            if el == 0:
                currMin, currMax = 1, 1
                res = max(res, el)
                continue
            tmp = currMax * el
            currMax = max(tmp, currMin * el, el)
            currMin = min(tmp, currMin * el, el)
            res = max(currMax, res)
        return res
