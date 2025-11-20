"""
```markdown
# Explanation of the Two Sum Solution

## 1. Brief Explanation of the Approach

The provided solution uses a hash map (dictionary in Python) to solve the "Two Sum" problem efficiently. The goal of the problem is to find two indices `i` and `j` in the list `nums` such that the sum of the numbers at those indices equals the `target`.

### Steps:
- Initialize an empty dictionary called `seen`.
- Iterate through the list `nums` using `enumerate()` to get both the index (`i`) and the value (`num`) at each step.
- For each `num`, calculate its complement (`target - num`).
- Check if this complement exists in the `seen` dictionary. If it does, return the indices of the complement and the current number as a list `[seen[complement], i]`.
- If the complement is not found, store the current number and its index in the `seen` dictionary.

This approach ensures that each number is processed in a single pass, allowing for quick lookups in the dictionary.

## 2. Time and Space Complexity Analysis

### Time Complexity:
- The time complexity of this solution is **O(N)**, where `N` is the number of elements in the `nums` list.
- This is because we iterate through the list once, while each dictionary operation (insertion and lookup) is on average O(1).

### Space Complexity:
- The space complexity is **O(N)** as well, in the worst case, we may need to store all `N` elements in the `seen` dictionary if no two sum solution is found.

## 3. Why this Approach is Efficient

This approach is efficient for a couple of reasons:
- **Single Pass**: It only requires a single loop through the list, making it linear in terms of time complexity, which is optimal for this problem compared to a brute-force solution that checks all pairs (which would take O(N^2) time).
- **Constant Time Lookups**: Using a hash map allows for quick checks to see if the complement of the current number has already been encountered, which is much faster than searching through a list.
- **Space Consideration**: The solution makes a trade-off by using extra space (the dictionary) to achieve significant time savings, which is generally acceptable given the constraints of the problem.

In conclusion, this solution efficiently finds the indices of the two numbers that add up to the target while maintaining a concise and clear implementation.
```

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
