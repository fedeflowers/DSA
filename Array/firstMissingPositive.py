"""
```markdown
## Explanation of the LeetCode Solution for "First Missing Positive"

### 1. Brief Explanation of the Approach
The solution implements an in-place algorithm to find the smallest missing positive integer from a given array of integers `nums`. The approach consists of two main steps:

1. **Rearranging the Array:** 
   The idea is to rearrange the elements in the array such that if `nums[i]` is a positive integer within the range of `1` to `n` (where `n` is the length of the array), then it should be placed at the index `nums[i] - 1`. This is done using a while loop that continues swapping elements until no more valid swaps can be made for the current position.

2. **Finding the Missing Positive:** 
   After the rearrangement, we iterate through the modified array to identify the first index `i` where the value does not equal `i + 1`. If such an index is found, it indicates that `i + 1` is the first missing positive integer. If all indices are correct, then the first missing positive integer must be `n + 1`.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** 
  The time complexity is O(n). In the first loop, we potentially swap each number at most once as we only rearrange the numbers to their correct positions. In the second loop, we traverse the array once to find the missing number, so each element is processed a constant number of times.

- **Space Complexity:**
  The space complexity is O(1) since we are rearranging the input array in place and not using any additional data structures that grow with the size of the input.

### 3. Why This Approach is Efficient
This approach is efficient because it leverages the properties of the input array to rearrange the numbers in such a way that we can identify the smallest missing positive integer in linear time and constant space. The key advantage of this method is that it avoids the overhead of using additional space for auxiliary data structures (like sets or hash tables), which is common in other solutions. Additionally, by utilizing in-place swaps, it efficiently categorizes and places each number into its corresponding index, making the check for the missing positive integer straightforward and quick.

Overall, this solution provides a balance between time efficiency and space efficiency, making it well-suited for situations where memory usage is a concern.
```

Runtime: undefined
Memory: 28848000
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
