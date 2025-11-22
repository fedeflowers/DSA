"""
```markdown
## Explanation of the Two Sum Solution

### 1. Brief Explanation of the Approach

The `twoSum` function aims to find two indices in the `nums` list such that the sum of the numbers at these indices equals the specified `target`. The approach utilizes a hash map (dictionary in Python) to store previously encountered numbers and their respective indices. 

As the function iterates through the `nums` list using an enumerated for loop, it checks if the difference between the `target` and the current number (`x`) already exists in the hash map (`vals`). If this difference exists, it means we have found two numbers that sum up to the `target`: the current number and the number stored in `vals`. The function then returns a list containing the current index and the index of the previously found number.

If the difference does not exist in the hash map, the current number along with its index is added to the hash map for future reference.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(n)
  - The function goes through each element in the `nums` array exactly once, resulting in a linear time complexity. The dictionary operations (insertion and lookup) are average O(1) due to the underlying implementation of hash maps in Python.

- **Space Complexity**: O(n)
  - In the worst case, if none of the pairs sum up to the target, all elements from the `nums` list will be stored in the hash map. This results in a linear space complexity.

### 3. Why this Approach is Efficient

This approach is efficient for several reasons:
- **Single Pass**: It reduces the need for nested loops which would lead to a O(n^2) complexity. By using a hash map for lookups, we can find the required complement for each number in constant time.
- **Immediate Result**: The moment we discover a valid pair that meets the criteria of the problem, we can immediately return the result without unnecessary calculations or iterations.
- **Dynamic Storage**: Utilizing a hash map dynamically stores indices of previously encountered numbers, thus allowing us to efficiently check for the necessary complement without re-scanning the list.

In summary, this implementation optimally combines time efficiency with straightforward logic to solve the Two Sum problem effectively.
```

Runtime: N/A
Memory: N/A
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
        
            

