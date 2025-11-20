"""
# Explanation of the Two Sum Solution

## 1. Approach Explanation

The solution utilizes a hash map (dictionary in Python) to efficiently find the indices of two numbers that add up to a specified target value. Here's a step-by-step breakdown of the approach:

- Initialize an empty dictionary called `seen` to map values to their respective indices as we iterate through the list `nums`.
- For each number in `nums`, calculate its complement by subtracting the number from the `target`.
- Check if the complement exists in the `seen` dictionary:
  - If it does, we have found the two numbers (the current number and its complement) that add up to the target. In this case, return the indices of the complement (from `seen`) and the current number.
  - If it does not exist, store the current number and its index in the `seen` dictionary.
- The loop continues until a solution is found, which guarantees that if the solution exists, it will be found in a single pass through the list.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - We only iterate over the list `nums` once. Each lookup and insertion operation in the dictionary (hash map) is average O(1), making the overall complexity linear with respect to the number of elements in `nums`.

- **Space Complexity**: O(N)
  - In the worst case, we store all N elements of the `nums` list in the `seen` dictionary, which consumes O(N) space.

## 3. Efficiency of the Approach

This approach is efficient because:

- **Single Pass**: Instead of using a nested loop to check each number against all others (which would result in O(N^2) time complexity), this algorithm processes each element only once.
- **Hash Map Lookup**: The use of a hash map allows for O(1) average time complexity for lookups, facilitating immediate checks for the existence of the needed complement for each number.
- **Immediate Solution Returning**: The algorithm immediately returns upon finding the first valid pair, which ensures it does not perform unnecessary computations after a solution is found.

In summary, the solution employs a clever combination of a single loop and a hash map to achieve an optimal solution for the Two Sum problem.

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
