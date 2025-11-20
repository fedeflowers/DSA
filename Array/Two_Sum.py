"""
## Explanation of the Two Sum Solution

### 1. Approach

The provided `twoSum` function uses a hash map (dictionary in Python) to keep track of the numbers that have been encountered so far in the list `nums`. The goal is to find two distinct indices `i` and `j` such that `nums[i] + nums[j] = target`.

Here's how the algorithm works step-by-step:

- Initialize an empty dictionary called `seen`, which will map each number to its index in the `nums` list.
- Iterate over the `nums` list using `enumerate`, which provides both the index `i` and the value `num` of each element.
- For each `num`, calculate its `complement`, which is the difference between the `target` and `num`.
- Check if this `complement` already exists in the `seen` dictionary:
  - If it does, that means we have already seen a number which, when added to `num`, equals `target`. Hence, we return the indices of both numbers: the index of the `complement` (found in `seen[complement]`) and the current index `i`.
- If the `complement` is not found, store `num` along with its index `i` in the `seen` dictionary for future reference.

### 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  
  The function iterates through the `nums` array exactly once, performing O(1) operations for checking membership in the dictionary and inserting into the dictionary for each element. Thus, the overall time complexity is linear with respect to the number of elements, N, in the `nums` array.

- **Space Complexity**: O(N)

  In the worst case, all the numbers in the `nums` list need to be stored in the `seen` dictionary. Therefore, in terms of space, the complexity is linear, O(N), as well.

### 3. Efficiency of the Approach

This approach is efficient for the following reasons:

- **Single Pass**: The algorithm solves the problem in a single pass through the array, which significantly reduces the time complexity compared to a brute-force solution that would require nested loops (O(N^2)).
- **Immediate Lookup**: By using a hash map, the algorithm allows for average O(1) time complexity for both insert and lookup operations. This enables quick checks for the existence of the `complement`.
- **Optimal for Unique Constraints**: While it assumes there are exactly one solution and does not handle duplicate elements differently, this method still effectively captures the solution under the typical assumption of the problem's constraints.

Overall, the use of a hash map provides a practical solution to the "Two Sum" problem, ensuring both efficiency and simplicity.

Runtime: N/A
Memory: N/A
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Hash map to store value: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
