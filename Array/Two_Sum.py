"""
## Explanation of the Solution for the "Two Sum" Problem

### 1. Brief Explanation of the Approach
The solution leverages a hash map (or dictionary in Python) to keep track of the indices of the numbers we encounter while iterating through the input list `nums`. The key concept is to look for the "complement" of each number, which is the value that, when added to the current number, equals the target.

Here’s how the algorithm works:
- Initialize an empty dictionary `seen` to store numbers and their corresponding indices.
- Loop through each number in the list `nums` using the index `i`:
  - Calculate the `complement` of the current number as `target - num`.
  - Check if this `complement` already exists in the `seen` dictionary. If it does, it means we have already encountered a number which can pair with the current number to reach the `target`, and we can return their indices.
  - If the `complement` is not found, add the current number and its index to the `seen` dictionary.

This method ensures that we find the solution in a single pass through the list.

### 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - We traverse the list `nums` once, where N is the length of the list. The operations involved (checking for existence in the dictionary and inserting into the dictionary) are on average O(1) because dictionary lookups and inserts are constant time operations.

- **Space Complexity**: O(N)
  - In the worst case, we may store every number in the `seen` dictionary, which may use up to O(N) space, where N is the length of the input list.

### 3. Why This Approach is Efficient
This approach is efficient because:
- It only requires a single pass through the input list, resulting in a linear time complexity relative to the size of the input. This is much more optimal than a naive approach that checks every possible pair of numbers to find the target sum, which would be O(N^2).
- The use of a hash map allows for quick lookups to check for the existence of a required complement, greatly reducing the time needed to find pairs that sum to the target.
- It elegantly balances time and space, providing an optimal solution without the need for additional sorting or nested loops.

This combination of factors makes this solution particularly suitable for the "Two Sum" problem, where multiple test cases might contain large lists of integers.

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
