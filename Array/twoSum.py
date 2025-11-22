"""
## Explanation of the Two Sum Solution

### 1. A brief explanation of the approach

The provided solution uses a hash map (dictionary in Python) to efficiently find two indices of numbers in the `nums` list that sum up to a specified `target`. The algorithm iterates through the list of numbers while maintaining a record of the indices of the numbers seen so far.

- For each number `x` in `nums`, the code calculates the difference between `target` and `x` (`target - x`). 
- It then checks if this difference is already present in the hash map (`vals`). If it is found, that means the current number `x` and the number corresponding to the stored index form a valid pair that sums to `target`.
- If the pair is found, the function returns the current index `i` and the index of the previously stored value.
- If not, it stores the current number `x` as a key in the hash map with its index `i` as the value for future lookups.

### 2. Time and Space Complexity analysis

- **Time Complexity**: O(n)
  - The algorithm iterates through the `nums` array exactly once. Each lookup and insertion in the hash map (dictionary) has an average time complexity of O(1). Therefore, the overall time complexity is linear, O(n), where `n` is the number of elements in the input list `nums`.

- **Space Complexity**: O(n)
  - In the worst case, the algorithm stores all `n` elements in the hash map if no two elements sum to the `target`. Thus, the space complexity is O(n) as well.

### 3. Why this approach is efficient

This approach is efficient for a few key reasons:

- **Single Pass**: The algorithm only requires a single pass through the input list, making it faster than solutions that may involve nested loops with O(n^2) time complexity.
- **Constant Time Lookup**: By using a hash map, the solution can achieve constant time complexity for both checking if the complement exists and storing indices, making it optimal for this problem.
- **Scalability**: The linear time complexity ensures that the algorithm can handle large input sizes efficiently without a bottleneck in performance, unlike a quadratic approach.

In summary, this solution efficiently utilizes a hash map to maintain state while iterating through the list, making it not only optimal in terms of time complexity but also straightforward to implement.

Runtime: undefined
Memory: 19104000
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        vals = {}
        for i, x in enumerate(nums):
            if target - x in vals:
                return [i, vals[target - x]]
            vals[x] = i 
        return
        
            

