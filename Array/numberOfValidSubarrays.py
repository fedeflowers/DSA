"""
```markdown
## Explanation of the Solution for "Number of Valid Subarrays"

### 1. Brief Explanation of the Approach
The problem aims to find the number of valid subarrays in the input list `nums`. A valid subarray is defined as a contiguous part of the array where all elements are non-decreasing. 

The solution utilizes a stack to efficiently track indices of the elements in `nums`. The key idea is to iterate through the array while maintaining a stack that allows us to pop elements when we encounter a new element that is smaller than the element at the index on the top of the stack. By doing this, we can calculate how many valid subarrays end at the current index `i`.

Here's a step-by-step explanation of how the solution works:
- The array is appended with `-1` at the end to ensure we can flush the stack at the end of the iteration.
- We initialize a result counter `res` to zero.
- We iterate over each element in `nums` using its index. For each element, we perform the following:
  - While the stack is not empty, and the current element `el` is smaller than the element at the index stored at the top of the stack (`nums[stack[-1]]`), we pop the index off the stack and add to `res` the difference between the current index `i` and the popped index. This gives the number of valid subarrays that can be formed using the popped index.
  - Finally, the current index `i` is pushed onto the stack.
- After going through all the elements, `res` will contain the total number of valid subarrays.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - The function processes each element at most twice (once when it is pushed onto the stack and once when it is popped), resulting in a linear time complexity of O(N), where N is the length of the input array.
  
- **Space Complexity**: O(N)
  - In the worst case, all elements are pushed onto the stack without being popped, leading to a space complexity of O(N).

### 3. Why this Approach is Efficient
This approach is efficient because:
- It uses a stack to maintain a dynamic list of indices representing elements that can potentially form valid subarrays. The stack enables efficient popping, allowing us to quickly determine the count of valid subarrays that can be formed with `el`.
- By combining the index manipulation and stack operations, we efficiently count valid subarrays without needing to check every possible subarray explicitly, avoiding a brute-force O(N^2) solution.
- The algorithm processes each element a limited number of times, allowing for a linear runtime, which is optimal for this type of problem.

Overall, the use of a stack provides both speed and clarity to determine the number of valid subarrays, making this solution well-suited for the given problem. 
```

Runtime: N/A
Memory: N/A
"""

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nums.append(-1) #flush at the end
        stack = []
        res = 0
        for i, el in enumerate(nums):
            while stack and el < nums[stack[-1]]:
                res += i - stack.pop()
            stack.append(i)

        return res



