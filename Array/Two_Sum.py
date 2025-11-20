"""
# Explanation of the Two Sum Solution

## 1. Brief Explanation of the Approach

The provided solution for the "Two Sum" problem uses a hash map (dictionary in Python) to keep track of the numbers we have seen so far and their corresponding indices. The algorithm works as follows:

- Iterate through each number in the input list `nums` using `enumerate` which gives both the index (`i`) and the number (`num`).
- For each number, compute the `complement` which is the difference between the `target` and the current `num` (i.e., `complement = target - num`).
- Check if this `complement` already exists in the `seen` hash map:
  - If it does, return the index of the `complement` (found in `seen`) and the current index `i`, as these two numbers add up to the target.
  - If it does not, store the current number `num` and its index `i` in the `seen` hash map.
  
This approach allows us to find two indices whose values sum to the target efficiently by leveraging the hash map for quick lookups.

## 2. Time and Space Complexity Analysis

- **Time Complexity**: O(N)
  - The algorithm makes a single pass through the list of numbers, performing constant time operations (dictionary lookups and insertions) for each element. Thus, the total time complexity is linear in terms of the number of elements, `N`.

- **Space Complexity**: O(N)
  - In the worst case, all the numbers are stored in the hash map if no two numbers add up to the target. Therefore, the space complexity is also linear in terms of the number of elements, `N`, due to the additional space used for the hash map.

## 3. Why This Approach is Efficient

This approach is efficient due to the following reasons:

- **Single Pass**: It only requires a single pass through the input list, which reduces the time complexity from O(N^2) (as in a naive nested loop approach) to O(N). This is a significant improvement, especially for large input sizes.
  
- **Fast Lookups**: Hash maps provide average-case constant time complexity for lookups and insertions. This allows for quick checks to see if the required complement exists for the current number.

- **Low Overhead**: The use of a hash map instead of more complex data structures keeps the implementation simple and the overhead low.

Overall, this solution effectively balances time and space efficiency, making it a commonly accepted method for solving the "Two Sum" problem.

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
