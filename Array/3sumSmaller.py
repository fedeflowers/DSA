"""
```markdown
## Explanation of the "3Sum Smaller" Solution

### 1. Brief Explanation of the Approach

The problem "3Sum Smaller" asks us to count the number of triplets (i, j, k) in an array such that the sum of the triplet is less than a given target. The solution uses a combination of sorting and a two-pointer technique. 

Here's how the approach works:

- **Sort the Array**: Initially, we sort the input array to facilitate the two-pointer technique.
  
- **Iterate through the Array**: We iterate through the elements of the array up to the third-to-last element (to ensure we can form triplets).
  
- **Two Pointer Technique**:
  - For each element at index `i`, we use two pointers: one (`left`) that starts just after `i` and another (`right`) that starts at the end of the array.
  - We compute the sum of the elements at these three indices (`i`, `left`, and `right`).
  - If this sum is less than the target, it indicates that all triplets with the current `i` and `left` are valid pairs with any element from the `left` to the `right` index (since the array is sorted). Hence, we can increment the result `res` by `right - left` and move the `left` pointer to the right.
  - If the sum is greater than or equal to the target, we need to decrease the sum. Therefore, we move the `right` pointer one position to the left.
  
- This process continues until the `left` pointer is no longer less than the `right` pointer.

At the end of all loops, `res` contains the count of all valid triplet combinations.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n^2)
  - The outer loop runs `n` times, and for each iteration of the outer loop, the inner while loop potentially runs up to `n` times (specifically, it runs in a linear fashion, reducing the search space). Thus, the overall time complexity is O(n^2).

- **Space Complexity**: O(1)
  - The algorithm uses a constant amount of space (excluding the input storage) since we are only using a few variables to keep track of indices and the result. The sorting operation is done in place (or typically requires O(n log n) for the sorting but does not affect the space complexity concerning additional variables used).

### 3. Why This Approach is Efficient

This approach is efficient because it leverages sorting and the two-pointer technique to reduce the potential number of triplets we would need to check directly. Instead of checking each triplet individually, which would lead to a cubic time complexity in a brute-force solution, the sorted array allows the algorithm to skip over many non-promising combinations quickly:

- By sorting the array, it becomes easy to determine when the sum of a chosen triplet exceeds the target (allowing us to simply move the pointers).
- Instead of checking each possible combination explicitly, the two-pointer method allows us to efficiently count valid combinations without redundant calculations.

This makes the solution not only elegant but well-optimized for larger datasets, significantly improving performance over naive approaches.
```

Runtime: undefined
Memory: 17880000
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 3 :
            return 0

        nums.sort()
        res = 0
        for i in range(n-2):
            right = n-1
            left = i+1
            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    res += right - left #valid for all triplets in between
                    left += 1
                else:
                    right -= 1

        return res


        


