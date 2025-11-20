"""
## Explanation of the LeetCode Solution for "Two Sum"

### 1. Brief Explanation of the Approach
The provided solution uses a hash map (dictionary in Python) to efficiently find two numbers in the list `nums` that sum up to the specified `target`. Here's how it works:

- Iterate through each number in the input list `nums` using the `enumerate` function, which gives both the index (`i`) and the number (`num`).
- For each number, calculate its "complement," which is defined as the difference between the `target` and the current number (`complement = target - num`).
- Check if this complement already exists in the `seen` dictionary. If it does, this means we have found the two numbers (the current number and its complement) that add up to the `target`. The indices of these numbers are returned as a list.
- If the complement does not exist in `seen`, store the current number and its index in the dictionary (`seen[num] = i`). This way, you keep track of the numbers you've already encountered and their corresponding indices.

### 2. Time and Space Complexity Analysis
- **Time Complexity:** O(n)
  - The solution iterates through the list `nums` exactly once, where `n` is the number of elements in `nums`. Each lookup in the hash map (to check for the complement) and insertion (to add current number and index) is on average O(1), leading to an overall linear time complexity.
  
- **Space Complexity:** O(n)
  - In the worst case, if no two numbers sum up to `target`, we would end up storing all `n` numbers in the `seen` dictionary. Therefore, the space complexity is also linear in relation to the size of the input list.

### 3. Why This Approach is Efficient
This approach is efficient for several reasons:

- **Single Pass Solution:** The algorithm makes only one pass through the input list, which minimizes the number of iterations and comparisons. This is crucial for performance, especially with large inputs.
- **Constant Time Lookups:** Using a hash map allows for average-case constant time complexity for both insertions and lookups, significantly speeding up the search for complements compared to a brute-force solution, which would require a nested loop with O(n^2) time complexity.
- **Immediate Return:** The solution returns immediately upon finding the two indices, further optimizing performance since it does not need to continue checking the rest of the list once a valid pair is found.

Overall, the combination of these elements results in an efficient and effective solution to the "Two Sum" problem.

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
