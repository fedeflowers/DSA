"""
# Two Sum Solution Explanation

## 1. Brief Explanation of the Approach
The provided solution employs a hash map (dictionary in Python) to efficiently determine if there are two numbers in the list `nums` that add up to a specified `target` value. The algorithm works by iterating through each number in the list while simultaneously keeping track of the indices of the numbers that have been processed.

Here’s a step-by-step breakdown of the approach:
- Initialize an empty hash map called `seen` that will store numbers as keys and their respective indices as values.
- Iterate through each number in the list `nums` using `enumerate` to get both the index `i` and the current number `num`.
- For each number, calculate its complement needed to reach the `target`, which is `target - num`.
- Check if this complement already exists in the `seen` hash map:
  - If it does, this means we have found two numbers (the current number `num` and its complement) that sum up to `target`. We then return their indices.
  - If it doesn't, we record the current number and its index in the `seen` map to use it for future iterations.

## 2. Time and Space Complexity Analysis
- **Time Complexity**: O(N)
  - The algorithm loops through the list of numbers exactly once. Each operation inside the loop (checking existence in the hash map and adding elements to it) takes average O(1) time. Therefore, the total time complexity is linear with respect to the size of the input list `nums`.
  
- **Space Complexity**: O(N)
  - In the worst case, we may end up storing all numbers from the input list in the hash map. Therefore, the space used grows linearly with the size of the list.

## 3. Why This Approach is Efficient
This approach is efficient due to its use of a hash map which allows for average O(1) time complexity for both insertions and look-ups. By storing previously seen numbers, it reduces the need for nested loops (which would have led to O(N^2) time complexity) and allows us to find the needed complement in constant time. This method ensures that we only go through the list once, making it optimal for finding a solution to the Two Sum problem while maintaining space efficiency through the use of a dynamic data structure (the hash map). 

Overall, this linear time solution with hash map utilization is a significant improvement over less efficient methods.

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
