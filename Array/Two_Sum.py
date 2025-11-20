"""
# Explanation of the Two Sum Solution

## 1. Brief Explanation of the Approach

The given solution utilizes a hash map (or dictionary) to efficiently find two numbers in the list `nums` that add up to a specified `target`. The algorithm follows these steps:

- Create a hash map named `seen` to store each number's value as the key and its index as the value.
- Iterate over the list `nums` using the `enumerate` function, which provides both the index (`i`) and the number (`num`).
- For each `num`, calculate its complement with respect to the target (`complement = target - num`).
- Check if this `complement` already exists in the `seen` hash map.
  - If it does, it means we found two numbers that add up to the target: `num` and its complement. The algorithm then returns their indices in the form of a list.
  - If it does not, the current number `num` and its index `i` are added to the `seen` hash map for future reference.

This approach ensures that each number is only processed once, which leads to an efficient solution.

## 2. Time and Space Complexity Analysis

### Time Complexity
- The algorithm runs in \(O(n)\), where \(n\) is the number of elements in the `nums` list. This is because we traverse the list exactly once and each lookup and insertion operation in the hash map is \(O(1)\) on average.

### Space Complexity
- The space complexity is also \(O(n)\) due to the additional hash map used to store elements and their indices. In the worst case, if no two numbers sum up to the target, we would store all \(n\) numbers in the hash map.

## 3. Why This Approach is Efficient

This approach is efficient due to the use of a hash map for constant time lookups and insertions. Instead of using a nested loop to check every possible pair of numbers (which would result in a time complexity of \(O(n^2)\)), this algorithm reduces the problem to a single pass through the data, significantly improving performance, especially for large datasets. By utilizing the hash map effectively, it achieves both hunting for the necessary complement and storing the indices of already seen numbers simultaneously, thus ensuring a quick and optimal solution.

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
